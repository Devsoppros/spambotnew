import os

class API:
    API_ID = int("8460373")
    API_HASH = "83d8e423197251216303abfcbed9e820"

class TOKENS:
    BOT_TOKEN = "5214157920:AAHuV_HOK7N6f05qGme0fPGcT8zPS6sHKYA"
    BOT_TOKEN_2 = "5816852248:AAFsGnME5H5nt6y_5eH1PFiOoIYt5P-cuPo"
    BOT_TOKEN_3 = "5312102248:AAFXteUlEB-aWBJgTB_BF6kxFcaDNX02Hfw"
    BOT_TOKEN_4 = "5378222617:AAF0uHAVd1Rtqt5kzMmCIFZtv_Au5WB7DqM"
    BOT_TOKEN_5 = "5216767657:AAFDZGIsdjcQf4hKx3gFXL3qMg78kqVcBFo"
    BOT_TOKEN_6 = "5132044795:AAHXkYsT1HLvPOEsNN3B7l9tekJvrVZknwg"
    BOT_TOKEN_7 = "5248088501:AAHMH1jwe5hSj3MI3rvU7qRrFPTmHckh1EU"
    BOT_TOKEN_8 = "5230151920:AAHhD1dPy0JlNSIUBLHDrsJD3ICMdUSyvqY"
    BOT_TOKEN_9 = "5298933528:AAE-744vuXparWYh4UV8y65IeT5wOhsw0zg"
    BOT_TOKEN_10 = "5574404365:AAEGW4ZJlsZBrjkKdI5HfqHf7tVzAI82pX4"

class DATABASE:
    MONGO_DB_URL = "mongodb+srv://Lightyagami10:light@cluster0.zo6bf4g.mongodb.net/?retryWrites=true&w=majority"

class DEV:
    OWNER_ID = int("1233641093")
    
    # DONT EDIT THIS 
    SUDO_USERS = [5834211089] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = "https://te.legra.ph/file/1069a942f7b0d3550b1b0.jpg"
    HELP_PIC = "https://te.legra.ph/file/7d694172191de4754a286.jpg"
    START_PIC = "https://te.legra.ph/file/1b188edbf455d2bafcf70.jpg"
    COMMAND_HANDLER = "!"
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # REPLACE 'True' BY 'False' IF U WANT TO DISABLE PORN
