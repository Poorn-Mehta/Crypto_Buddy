# Set the path to chromedriver
# For example: CHROMEDRIVER_LOCAL_PATH = "C:/Users/poorn/AppData/Local/Programs/Python/chromedriver.exe"
CHROMEDRIVER_LOCAL_PATH = "C:/Users/poorn/AppData/Local/Programs/Python/chromedriver.exe"

# Set the path to excel file
# For example: EXCEL_FILE_SRC_FOLDER_PATH = "C:/Users/poorn/Desktop/Files/Crypto/" and 
# You can leave EXCEL_FILE_SRC_FOLDER_PATH if Crypto.py, Crypto_Config.py and xlsx file are in same folder
EXCEL_FILE_SRC_FOLDER_PATH = "C:/Users/poorn/Desktop/Files/Crypto/"

# Name of spreadsheet
EXCEL_FILE_NAME_WITH_EXTENSION = "Investments.xlsx"

# You can edit the following variables as per your convenience 
# I don't recommend changing unless you know what you're doing
# I will probably add comments describing what each one of them does in future
# Feel free to ask me if you want to customize but are facing issues
EXCEL_SPREADSHEET_NAME = "Crypto"
EXCEL_ASSET_IDENTIFIER = "Asset"
EXCEL_COLUMNS_RANGE_FOR_ASSET = 10 # > 26 not supported
EXCEL_CURRENT_PRICE_IDENTIFIER = "Current"
EXCEL_COLUMNS_RANGE_FOR_CURRENT_PRICE = 20 # > 26 not supported
EXCEL_PERCENT_INDENTIFIER = "Percent Change"
EXCEL_COLUMNS_RANGE_FOR_PERCENT = 20 # > 26 not supported
EXCEL_MAX_CRYPTO_ASSETS = 110
EXCEL_MAX_ROWS_FOR_IDENTIFIER = 5
EXCEL_ALERT_IDENTIFIERS = ["PH", "PL", "PU", "PD"]
EXCEL_ALERT_VAL_HIGH_IDENTIFIER_INDEX = 0
EXCEL_ALERT_VAL_LOW_IDENTIFIER_INDEX = 1
EXCEL_ALERT_PERC_UP_IDENTIFIER_INDEX = 2
EXCEL_ALERT_PERC_DOWN_IDENTIFIER_INDEX = 3
EXCEL_COLUMNS_RANGE_FOR_ALERTS = 20	# > 26 not supported
EXCEL_ALERTS_MAX_PER_CATEGORY = 10
EXCEL_ALERT_CATEGORY_COUNT = 4
EXCEL_ALERT_INVALID = 0

# Add information from Sinch
# For phone numbers, pay attention to format (e.g. +1(123)456-7890 should be entered as SINCH_SOURCE_PHONE_NUMBER = "11234567890")
# Source phone number will be the one that you 'pick' when signing up for Sinch SMS
# Target phone number is your own
# While setting up Sinch SMS, you will at some point get Service ID and Token
SINCH_SOURCE_PHONE_NUMBER = "14356776951"
SINCH_TARGET_PHONE_NUMBER = "17209400389"
SINCH_SERVICE_ID = "4a3aa6343da1433c81b9de26de4c8dd8"
SINCH_TOKEN = "dcac07a3e4e14ab3926503d0e7d4b196"

# Set the refresh speed, by default it is 1 minutes (60 seconds)
POLLING_INTERVAL_DEFAULT_TIME_SECONDS = 60	# > 3600 not supported (Sinch refresh)

# To close after x number of seconds after Enter key is detected (2 for now)
SCRIPT_EXIT_DELAY_SECONDS = 2

# If your crypto is not anywhere in this list, it will not be able to pull latest price from coingecko
# Add the last part of full URL in here, for example ETH is at https://www.coingecko.com/en/coins/ethereum
# So you add "ETH"  : "ethereum" in following dictionary
CRYPTO_LOOKUP = {
	"BTC"  : "bitcoin",
	"ETH"  : "ethereum",
	"XRP"  : "xrp",
	"BCH"  : "bitcoin-cash",
	"ADA"  : "cardano",
	"BSV"  : "bitcoin-sv",
	"LINK" : "chainlink",
	"LTC"  : "litecoin",
	"CRO"  : "crypto-com-coin",
	"BNB"  : "binance-coin",
	"EOS"  : "eos",
	"XTZ"  : "tezos",
	"XLM"  : "stellar",
	"OKB"  : "okb",
	"XMR"  : "monero",
	"VET"  : "vechain",
	"TRX"  : "tron",
	"LEO"  : "leo-token",
	"HT"   : "huobi-token",
	"ATOM" : "cosmos",
	"CDAI" : "compound-dai",
	"NEO"  : "neo",
	"ETC"  : "ethereum-classic",
	"MIOTA": "iota",
	"DASH" : "dash",
	"ZEC"  : "zcash",
	"COMP" : "compound",
	"ONT"  : "ontology",
	"XEM"  : "nem",
	"DOGE" : "dogecoin",
	"LEND" : "aave",
	"MKR"  : "maker",
	"BAT"  : "basic-attention-token",
	"SNX"  : "synthetix-network-token",
	"KNC"  : "kyber-network",
	"ZRX"  : "0x",
	"FTT"  : "ftx-token",
	"ALGO" : "algorand",
	"DGB"  : "digibyte",
	"THETA": "theta-network",
	"QTUM" : "qtum",
	"CETH" : "compound-ether",
	"PAX"  : "paxos-standard",
	"AMPL" : "ampleforth",
	"OMG"  : "omg-network",
	"ICX"  : "icx",
	"REP"  : "augur",
	"ERD"  : "elrond",
	"ZIL"  : "zilliqa",
	"HBAR" : "hedera-hashgraph",
	"ENJ"  : "enjin-coin",
	"DCR"  : "decred",
	"LSK"  : "lisk",
	"BCD"  : "bitcoin-diamond",
	"BTG"  : "bitcoin-gold",
	"LRC"  : "loopring",
	"SC"   : "siacoin",
	"REN"  : "ren",
	"CEL"  : "cel",
	"BTM"  : "bytom",
	"WAVES": "waves",
	"HYN"  : "hyperion",
	"RVN"  : "ravencoin",
	"NANO" : "nano",
	"DIVI" : "divi",
	"HOT"  : "holo",
	"MONA" : "monacoin",
	"RLC"  : "iexec-rlc",
	"LUNA" : "terra-luna",
	"STX"  : "blockstack",
	"NEXO" : "nexo",
	"BNT"  : "bancor-network",
	"CKB"  : "nervos-network",
	"DX"   : "dxchain-token",
	"UMA"  : "uma",
	"SNT"  : "status",
	"NMR"  : "numeraire",
	"GT"   : "gatechain-token",
	"XVG"  : "verge",
	"CHSB" : "swissborg",
	"DGTX" : "digitex-futures-exchange",
	"IOST" : "iost",
	"RSR"  : "reserve-rights-token",
	"XAUT" : "tether-gold",
	"QNT"  : "quant",
	"BTT"  : "bittorrent",
	"RUNE" : "rune",
	"SXP"  : "swipe",
	"KMD"  : "komodo",
	"ALEND": "aave-lend",
	"MATIC": "matic-network",
	"HIVE" : "hive",
	"AOA"  : "aurora",
	"DMG"  : "dmm-governance",
	"AERGO": "aergo",
	"NPXS" : "pundi-x-old",
	"HEX"  : "hex",
	"NYZO" : "nyzo",
	"POLY" : "polymath-network",
	"MOON" : "moon-coin",
	"OMG"  : "omg-network",
	"QKC"  : "quarkchain",
	"CELR" : "celer-network",
	"OGN"  : "origin-protocol",
	"DAG"  : "constellation",
	"RCN"  : "ripio-credit-network",
#	"MCO"  : "mco",
	"AKRO" : "akropolis",
	"ZEL"  : "zelcash",
	"ADB"  : "adbank",
	"MLN"  : "melon",
	"MCB"  : "mcdex",
	"REL"  : "relevant",
	"TOMO" : "tomochain",
	"COTI" : "coti",
	"PCX"  : "chainx",
	"SRK"  : "sparkpoint",
	"DOS"  : "dos-network",
	"CEEK" : "ceek-smart-vr-token",
	"DOT"  : "polkadot",
	"SWAP" : "trustswap",
	"FRM"  : "ferrum-network",
	"EDG"  : "edgeware",
	"DAPS" : "daps-coin",
	"CRPT" : "crypterium",
	"SXP"  : "swipe",
	"UTK"  : "utrust",
	"SBREE": "cbdao",
	"FTM"  : "fantom",
	"ZEN"  : "horizen",
	"PERX" : "peerex-network",
	"DIA"  : "dia",
	"ESS"  : "essentia",
	"FERA" : "fera",
	"TRADE": "unitrade",
	"OM"   : "mantra-dao",
	"WOM"  : "wom-protocol",
	"PASTA": "spaghetti",
	"YFT"  : "yield-farming-token",
	"UNCX" : "unicrypt",
	"PYLON": "pylon-finance",
	"YFT"  : "yield-farming-token",
	"EFX"  : "effect-ai",
	"CHR"  : "chromia",
	"ANKR" : "ankr-network",
	"BID"  : "bidao",
	"UNI"  : "uniswap",
	"N3RD" : "n3rd-finance",
	"PAR"  : "parachute",
	"MCP"  : "my-crypto-play",
	"RAMP" : "ramp",
	"INJ"  : "injective-protocol",
	"KAI"  : "kardiachain",
	"RING" : "darwinia-network-native-token",
	"MIR"  : "mirror-protocol",
	"MP3"  : "mp3",
	"LIT"  : "litentry",
	"DEOR" : "decentralized-oracle",
	"GDAO" : "governor-dao",
	"YFSI" : "yfscience",
	"KEK"  : "cryptokek",
	"MOD"  : "modefi",
	"BART" : "bartertrade",
	"UDO"  : "unido",
	"NDS"  : "nodeseeds"
}