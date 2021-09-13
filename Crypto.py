import sys, time, os, msvcrt, xlwings, requests, json                    

import Crypto_Config as CC

# Constants
TARGET_COINGECKO_API_ID_START = "https://api.coingecko.com/api/v3/simple/price?ids="
TARGET_COINGECKO_API_PRICE_START = "&vs_currencies="

NUMBER_OF_ALPHABETS = 26
CAPITAL_A_ASCII = 65
ENTER_KEY_ASCII = 13

SMS_REFRESH_INTERVAL_SECONDS = 600

# Config
XLSX_FILE = CC.EXCEL_FILE_SRC_FOLDER_PATH + CC.EXCEL_FILE_NAME_WITH_EXTENSION
SPREADSHEET_NAME = CC.EXCEL_SPREADSHEET_NAME
ASSET_ID = CC.EXCEL_ASSET_IDENTIFIER
ASSET_COLS = CC.EXCEL_COLUMNS_RANGE_FOR_ASSET
CURRENT_PRICE_ID = CC.EXCEL_CURRENT_PRICE_IDENTIFIER
CURRENT_PRICE_COLS = CC.EXCEL_COLUMNS_RANGE_FOR_CURRENT_PRICE
PERCENT_ID = CC.EXCEL_PERCENT_INDENTIFIER
PERCENT_COLS = CC.EXCEL_COLUMNS_RANGE_FOR_PERCENT
ASSETS_MAX = CC.EXCEL_MAX_CRYPTO_ASSETS
COINGECKO_MAX = CC.EXCEL_MAX_COINGECKO_ASSETS
ROWS_ID_MAX = CC.EXCEL_MAX_ROWS_FOR_IDENTIFIER
ALERT_IDS = CC.EXCEL_ALERT_IDENTIFIERS
ALERT_PH_ID = CC.EXCEL_ALERT_VAL_HIGH_IDENTIFIER_INDEX
ALERT_PL_ID = CC.EXCEL_ALERT_VAL_LOW_IDENTIFIER_INDEX
ALERT_PU_ID = CC.EXCEL_ALERT_PERC_UP_IDENTIFIER_INDEX
ALERT_PD_ID = CC.EXCEL_ALERT_PERC_DOWN_IDENTIFIER_INDEX
ALERT_COLS = CC.EXCEL_COLUMNS_RANGE_FOR_ALERTS
ALERT_MAX = CC.EXCEL_ALERTS_MAX_PER_CATEGORY
ALERT_COUNT = CC.EXCEL_ALERT_CATEGORY_COUNT
ALERT_INVALID = CC.EXCEL_ALERT_INVALID
TIMEOUT = CC.POLLING_INTERVAL_DEFAULT_TIME_SECONDS
EXIT_DELAY = CC.SCRIPT_EXIT_DELAY_SECONDS
ASSET_LUT = CC.CRYPTO_LOOKUP

if (ASSETS_MAX % COINGECKO_MAX) != 0:
	API_ARR_SIZE = int(ASSETS_MAX / COINGECKO_MAX) + 1
else:
	API_ARR_SIZE = int(ASSETS_MAX / COINGECKO_MAX)

# Global Variables
coingecko_api_arr = [""] * API_ARR_SIZE
my_workbook = None
crypto_spreadsheet = None
crypto_mylist = []
asset_info = {
	"cell"    : "",
	"column"  : "",
	"row_num" : 0,
	"found"   : 0
}
current_price_info = {
	"cell"    : "",
	"column"  : "",
	"row_num" : 0,
	"found"   : 0
}
percent_info = {
	"cell"    : "",
	"column"  : "",
	"found"   : 0
}
append_string = None
sinch_client = None
sinch_sms_handler = None
alert_cells = [["" for col in range(ALERT_MAX)] for row in range(ALERT_COUNT)]
sms_refresh_counter = 0

def Excel_Init():

	print("Setting up Excel...")

	global my_workbook, crypto_spreadsheet

	my_workbook = xlwings.Book(XLSX_FILE)
	crypto_spreadsheet = my_workbook.sheets[SPREADSHEET_NAME]

	return None

def Excel_Num_To_Col_Name(number):

	col_name = ""

	while number > 0:

		number, remainder = divmod ((number - 1), NUMBER_OF_ALPHABETS) 
		col_name = chr(remainder + CAPITAL_A_ASCII) + col_name

	return col_name

def Excel_Col_Name_To_Num(name):
	
	number = 0
	
	for character in name:

		number = (number * NUMBER_OF_ALPHABETS) + (ord(character) - CAPITAL_A_ASCII) + 1 

	return number

def Find_Target_Column_Start_Row(col_range, identifier, custom_col_start = 0):

	global crypto_spreadsheet

	return_cell = ""
	return_found = 0
	col_range_str = ""

	for x in range(custom_col_start, col_range):
		col_range_str = col_range_str + Excel_Num_To_Col_Name(x + 1)

	for row in range(1, ROWS_ID_MAX):

		for column in col_range_str:	# potential bottleneck here for searching after column 'Z'

			return_cell = "{}{}".format(column, row)

			if crypto_spreadsheet.range(return_cell).value == identifier:

				return_found = 1
				break

		if return_found == 1:

			break

	if return_found == 0:

		return_cell = ""

	return return_cell

def Get_Asset_Cell():

	print("Looking for Asset Column in {} Spreadsheet...".format(SPREADSHEET_NAME))

	global asset_info

	asset_info["cell"] = Find_Target_Column_Start_Row(ASSET_COLS, ASSET_ID)

	if asset_info["cell"] != "":

		asset_info["found"] = 1
		asset_info["column"] = asset_info["cell"][0:1] # potential bottleneck here for columns after'Z'
		asset_info["row_num"] = int(asset_info["cell"][1:]) + 1

	else:

		asset_info["found"] = 0

	return None

def Get_Current_Price_Cell():

	print("Looking for Current Prices Column in {} Spreadsheet...".format(SPREADSHEET_NAME))

	global current_price_info

	current_price_info["cell"] = Find_Target_Column_Start_Row(CURRENT_PRICE_COLS, CURRENT_PRICE_ID)

	if current_price_info["cell"] != "":

		current_price_info["found"] = 1
		current_price_info["column"] = current_price_info["cell"][0:1] # potential bottleneck here for columns after'Z'
		current_price_info["row_num"] = int(current_price_info["cell"][1:]) + 1

	else:

		current_price_info["found"] = 0

	return None

def Prepare_My_Crypto_List():

	print("Preparing Customized List of Crypto Assets...")

	global crypto_mylist, crypto_spreadsheet

	if asset_info["found"] == 1:

		for row in range(asset_info["row_num"], (asset_info["row_num"] + ASSETS_MAX)):

			for column in asset_info["column"]:

				asset_info["cell"] = "{}{}".format(column, row)
				append_string = crypto_spreadsheet.range(asset_info["cell"]).value

				if append_string is not None:

					crypto_mylist.append(append_string)

				else:

					row = asset_info["row_num"] + ASSETS_MAX
					break

	return None

def Desktop_Alert(crypto_name, alert_type, alert_value, current_value):

	alert_string = "Alert for {}!!! ".format(crypto_name)

	if (alert_type == ALERT_PH_ID):
		alert_string += "Price High Goal of ${} Reached with ${}".format(alert_value, current_value)
	elif (alert_type == ALERT_PL_ID):
		alert_string += "Price Low Goal of ${} Reached with ${}".format(alert_value, current_value)
	elif (alert_type == ALERT_PU_ID):
		perc_str = f"{current_value:.2f}"
		alert_string += "Percentage Up Goal of {}% Reached with {}%".format(alert_value, perc_str)
	elif (alert_type == ALERT_PD_ID):
		perc_str = f"{current_value:.2f}"
		alert_string += "Percentage Down Goal of {}% Reached with {}%".format(alert_value, perc_str)
	else:
		sms_alert_string += "Unknown Alert Type"

	print("Sending Alert: {}".format(alert_string))
	os.system(f"msg * {alert_string}")
def Setup_Alerts():
	
	print("Setting up Alerts...")

	global alert_cells, percent_info

	for alert_category in range(ALERT_COUNT):

		col_start = 0
		count = 0
		identifier = ""
		cell = ""

		for x in range(ALERT_COLS):

			identifier = ALERT_IDS[alert_category] + str(count + 1)
			cell = Find_Target_Column_Start_Row(ALERT_COLS, identifier, col_start)

			if cell != "":

				alert_cells[alert_category][count] = cell
				col_start = Excel_Col_Name_To_Num(alert_cells[alert_category][count][0:1]) # potential bottleneck here for columns after'Z'
				count += 1

	percent_info["cell"] = Find_Target_Column_Start_Row(PERCENT_COLS, PERCENT_ID)

	if percent_info["cell"] != "":

		percent_info["found"] = 1
		percent_info["column"] = percent_info["cell"][0:1] # potential bottleneck here for columns after'Z'

	else:

		percent_info["found"] = 0

	return None

def Handle_Alerts(crypto_name, current_price, row):
	
	global alert_cells, crypto_spreadsheet, percent_info

	alert_value_cell = ""
	alert_value = ALERT_INVALID
	percent_cell = "{}{}".format(percent_info["column"], row)
	percent = crypto_spreadsheet.range(percent_cell).value

	for x in range(ALERT_MAX):

		if alert_cells[ALERT_PH_ID][x] != "":

			column = alert_cells[ALERT_PH_ID][x][0:1] # potential bottleneck here for columns after'Z'
			alert_value_cell = "{}{}".format(column, row)
			alert_value = crypto_spreadsheet.range(alert_value_cell).value

			if (alert_value > ALERT_INVALID) and (current_price >= alert_value):
				
				Desktop_Alert(crypto_name, ALERT_PH_ID, alert_value, current_price)
				crypto_spreadsheet.range(alert_value_cell).value = ALERT_INVALID

	for x in range(ALERT_MAX):

		if alert_cells[ALERT_PL_ID][x] != "":

			column = alert_cells[ALERT_PL_ID][x][0:1] # potential bottleneck here for columns after'Z'
			alert_value_cell = "{}{}".format(column, row)
			alert_value = crypto_spreadsheet.range(alert_value_cell).value

			if (alert_value > ALERT_INVALID) and (current_price <= alert_value):
			
				Desktop_Alert(crypto_name, ALERT_PL_ID, alert_value, current_price)
				crypto_spreadsheet.range(alert_value_cell).value = ALERT_INVALID

	if percent is not None:

		for x in range(ALERT_MAX):

			if alert_cells[ALERT_PU_ID][x] != "":

				column = alert_cells[ALERT_PU_ID][x][0:1] # potential bottleneck here for columns after'Z'
				alert_value_cell = "{}{}".format(column, row)
				alert_value = crypto_spreadsheet.range(alert_value_cell).value * 100

				if (alert_value > ALERT_INVALID) and (percent > 0):

					if percent >= alert_value:
					
						Desktop_Alert(crypto_name, ALERT_PU_ID, alert_value, percent)
						crypto_spreadsheet.range(alert_value_cell).value = ALERT_INVALID

		for x in range(ALERT_MAX):

			if alert_cells[ALERT_PD_ID][x] != "":

				column = alert_cells[ALERT_PD_ID][x][0:1] # potential bottleneck here for columns after'Z'
				alert_value_cell = "{}{}".format(column, row)
				alert_value = crypto_spreadsheet.range(alert_value_cell).value * 100

				if (alert_value < ALERT_INVALID) and (alert_value > -100) and (percent < 0):

					if percent <= alert_value:
					
						Desktop_Alert(crypto_name, ALERT_PD_ID, alert_value, percent)
						crypto_spreadsheet.range(alert_value_cell).value = ALERT_INVALID

	return None

def Update_Crypto_Prices():

	global crypto_mylist, ASSET_LUT, ASSETS_MAX, browser, crypto_spreadsheet, coingecko_api_arr

	my_crypto_prices = [None] * API_ARR_SIZE
	my_crypto_prices_json = [None] * API_ARR_SIZE

	for api_index in range(API_ARR_SIZE):

		start_index = api_index * COINGECKO_MAX
		last_index = (api_index + 1) * COINGECKO_MAX

		if last_index >= len(crypto_mylist):

			last_index = len(crypto_mylist)

		coingecko_api_arr[api_index] = TARGET_COINGECKO_API_ID_START
		counter = start_index

		for my_crypto in range(start_index, last_index):

			if crypto_mylist[my_crypto].upper() in ASSET_LUT:

				coingecko_api_arr[api_index] += ASSET_LUT[crypto_mylist[my_crypto].upper()]
				coingecko_api_arr[api_index] += "%2C"
				counter += 1

			else:

				print("Error!! Crypto Asset " + crypto_mylist[my_crypto].upper() + " Not Added in the CRYPTO_LOOKUP")

		coingecko_api_arr[api_index] = coingecko_api_arr[api_index][:-3]
		coingecko_api_arr[api_index] += TARGET_COINGECKO_API_PRICE_START

		for x in range(start_index, counter):

			coingecko_api_arr[api_index] += "usd%2C"

		coingecko_api_arr[api_index] = coingecko_api_arr[api_index][:-3]

		my_crypto_prices[api_index] = requests.get(coingecko_api_arr[api_index])
		my_crypto_prices_json[api_index] = my_crypto_prices[api_index].json()

		if last_index == len(crypto_mylist):

			break

	for my_crypto in range(len(crypto_mylist)):

		if crypto_mylist[my_crypto].upper() in ASSET_LUT:

			target_json_index = 0
			temp_crypto = my_crypto

			while (temp_crypto >= COINGECKO_MAX):

				temp_crypto -= COINGECKO_MAX
				target_json_index += 1
			
			target_json = my_crypto_prices_json[target_json_index]
			value = target_json[ASSET_LUT[crypto_mylist[my_crypto].upper()]]["usd"]

			if value is not None:

				if value < 0.000001:
					my_crypto_price_flt = format(value, "0.15f")
				else:
					my_crypto_price_flt = float("{:f}".format(value))
				print("Current Price for " + crypto_mylist[my_crypto].upper() + " is: ${}".format(my_crypto_price_flt))

				if current_price_info["found"] == 1:

					for column in current_price_info["column"]:

						row = current_price_info["row_num"] + my_crypto
						market_price_cell = "{}{}".format(column, row)
						crypto_spreadsheet.range(market_price_cell).value = my_crypto_price_flt
						Handle_Alerts(crypto_mylist[my_crypto].upper(), my_crypto_price_flt, row)

			else:

				print("Error!! Crypto Asset " + ASSET_LUT[crypto_mylist[my_crypto].upper()] + " Not Found by CoinGecko API")

	return None

def Input_TIMEOUT():

	global TIMEOUT

	start_time = time.time()
	ip = ""
	retval = 0

	while 1:

		if msvcrt.kbhit():

			ip = msvcrt.getche()

			if ord(ip) == ENTER_KEY_ASCII:

				break

		if (time.time() - start_time) > TIMEOUT:

			break

	if len(ip) != 0:

		if ord(ip) == ENTER_KEY_ASCII:

			retval = 1

	else:

		retval = 0

	return retval

Excel_Init()
Get_Asset_Cell()
Get_Current_Price_Cell()
Prepare_My_Crypto_List()
Setup_Alerts()

while 1:

	_ = os.system("cls")
	print("Press Enter anytime to Terminate the Script (action taken at the end of cycle)")

	Update_Crypto_Prices()

	my_workbook.save(XLSX_FILE)
	print("Polling Interval is set to {} Seconds, Waiting...".format(TIMEOUT))

	sms_refresh_counter += 1

	if Input_TIMEOUT() == 1:

		break;

	else:

		if sms_refresh_counter >= (SMS_REFRESH_INTERVAL_SECONDS / TIMEOUT):

			sms_refresh_counter = 0

	print("End of Cycle")

print("Enter Detected!! Exiting in {} Seconds".format(EXIT_DELAY))
time.sleep(EXIT_DELAY)