# Crypto Buddy v1.1
## How-to Guide

### NOTE
This is a side-project I have developed for my own use. The primary purpose is to be able to set multiple price targets as well as percentage change goals - for as many crypto assets as you'd like, and get SMS alerts on your phone automatically (while the script is running). There might be much better tools available out there - offering this and much more, but I wanted to keep my portfolio in Excel and enjoy the development/learning process - so worked on this project. 
Please note that it is very limited in features, and uses quite the basic techniques that I have recently learned. I am a beginner in Python, so there are lots of areas of improvement in this. If you want to contribute, please reach out to me and I will be happy to add you as a collaborator. If you have any comments/feedback/reviews/feature requests/queries - feel free to contact me. It would be great to know the perception and impact of this project!

#### Contact Information
Discord (preferred): SPiiKeSS#8587
Email: Poorn.Mehta@Colorado.EDU

### Please go through this guide before utilizing tool
### This tool is intended for utilization on Windows with Python 3.x 
    Tested on Windows 10 with Python 3.8 and Excel 16


## Setup
#### Download the Investments.xlsx file provided in this repository as a starting point. Note the path of download (to be used in Crypto_Config.py)
#### Download Crypto.py and Crypto_Config.py files from this repository. It is advised that all of these files stay in same folder. 
#### Download and install [google chrome](https://www.google.com/chrome/) (if you already don't have it)
#### Download [chromedriver.exe](https://chromedriver.chromium.org/) Note the path of download (to be used in Crypto_Config.py)
#### Download and install Microsoft Visual C++ (latest) [Get it here](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 
#### You can also check out [this guide for more clarity](https://medium.com/@jacky_ttt/day060-fix-error-microsoft-visual-c-14-0-is-required-629413e798cd)
#### Setup your account on [Sinch](https://www.sinch.com/)
  * Create your account for SMS
  * A number of countries are supported, the service is paid - but quite useful and affordable
  * It will ask you to pick a phone number to send SMS from 
  * Once you pick the phone number and complete procedure, you will get your Sinch Service ID and Token Number. Save this both - will be needed later.
  * You will need to activate the account in order to edit the SMS text content, this process might take a few hours 
#### Download and install [Python for Windows](https://www.python.org/downloads/windows/)
  * I recommend using Windows x86-64 web-based installer
  * Please check the option "Add to PATH" which should come up once the setup is launched 
  * After installation, open windows cmd (type cmd in windows search bar and run), type "python" without quotes and press enter
  * You should see a text similar to this: Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
  * If you do see it, your python is correctly added to the PATH
  * If not, follow a guide [such as this](https://datatofish.com/add-python-to-windows-path/) to get it to work
  * Type exit() to get out of python shell
  * In cmd, type and execute following commands: 
    * python -m pip install --upgrade setuptools
    * python -m pip install selenium
    * python -m pip install xlwings
    * python -m pip install clx-sdk-xms
#### Edit Crypto_Config.py file using your favorite text editor
  * Thoroughly read each and every comment in Crypto_Config.py and make appropriate changes
  * Save the file before closing
#### Insert your data in Investments.xlsx
  * Spend some time familizarizing yourself with the spreadsheet, looking at internal links (in asset column), and various formulas used 
  * Columns D (Stored At) and F (Target) are optional
  * Column E (Buy) calculates your average 'bought at' price for every asset. Please note that if you sell for a profit, this number will go down, and if you sell for a loss, this number will go up. I set it up this way to see that after selling for a particular price - what is target price for breaking even. 
  * Column G (Current) is where the python script will write data of market price
  * PH1 and PH2 refers to Price High Targets. Entering amount in dollar here results in following: if current price is greater than or equal to the one listed in PH1/2 column - then it sends an SMS alert, and clears the price target in relevant row (based on asset) in PH1/2 column. This is done in order to prevent duplicate alerts.
  * PL stands for Price Down, PU stands for Percentage Up, and PD stands for Percentage Down. They are all designed for sending customized SMS alerts.
  * Please note that you can use it only for alerts as well - in which case you don't have to include information about all of the trades etc. In the simplest use case, add Asset symbol in Column A, and in the same row - set price targets. Set unused targets to 0. In order to use Percentage targets, you will have to have some value in Column E (Buy). 
  * You can also increase/decrease number of price and/or percentage targets. Simply add more columns with proper naming conventions (PH1, PH2, PH3 etc.)
  * There is a limitation however - in this project: Columns after Z (such as AA, AB etc.) are not scannable. I will try to support that in the future. So if you add too many targets and some of those column go beyond Z - it will never be triggered. 
#### Save everything, and run Crypto.py
  * Open windows command prompt/cmd
  * Navigate to the folder containing Crypto.py and Crypto_Config.py (they have to be in same location)
    * Use cd command for navigation [look this up if you're not familiar with it](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands)
  * Type: python Crypto.py - and press Enter
  * Keep it running if you want alerts. It might slow down your computer, so set the polling interval to a high number (~10 minutes or so). You can also press Enter key at any point to terminate the script (done at the end of a loop). You can terminate and restart as per your convenience. 
#### That's it! Have Fun! 
  
  
