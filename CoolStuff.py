#Nifty Functions
#By Brad Ayers
#February 2024 - Present

def DataFile(Filename):
    #This function automates the data file saving process, including a loading bar. Specify the name of the file as an arugment when calling the function.
    #DataFile("filename.dat")
    import types
    import time
    import random
    PHRASE_1 = "Saving: Please Stand By"
    PHRASE_2 = "Data Saved Successfully."
    DataList = []
    Frames1 = []
    Frames2 = []
    Frames3 = []
    def FrameLoop(Phrase, FrameList):
        #Just avoiding repetition within the outer function.
        Counter1 = 0
        Counter2 = 1
        while Counter1 <= len(Phrase):
            FrameList.append(Phrase[0:Counter2])
            Counter1 += 1
            Counter2 += 1
    AllVars = dict(globals())
    for Name, Var in AllVars.items():
        if type(Var) not in [types.ModuleType, types.FunctionType] and not Name.startswith("_"):
            DataList.append(Var)
    f = open(Filename, "a")
    for item in DataList:
        if item != DataList[-1]:
            f.write("{},".format(str(item)))
        else:
            f.write("{}\n".format(str(item)))
    f.close()
    FrameLoop(PHRASE_1, Frames1)
    for i in range(0,3):
        for j in range(0,4):
            Frames1.append(PHRASE_1 + (j * " ."))    
    for i in range(0,41):
        Frames2.append(i * "|")
    FrameLoop(PHRASE_2, Frames3)
    for frame in Frames1:
        print("\r" + frame, end="")
        time.sleep(0.03)
    print("\r" + " " * len(Frames1[-1]), end="")
    LoadingDelay = random.randint(20,34)
    for frame in Frames2:
        if frame == Frames2[LoadingDelay]:
            print("\r" + frame, end="")
            time.sleep(random.uniform(0.6, 0.9))
        else:
            print("\r" + frame, end="")
            time.sleep(0.05)
    print("\r" + " " * len(Frames2[-1]), end="")
    for frame in Frames3:
        if frame != Frames3[-1]:
            print("\r" + frame, end="")
            time.sleep(0.03)
        else:
            print("\r" + frame, end="")
            time.sleep(0.5)
    print("\r" + " " * len(Frames3[-1]), end="")
    
def Hst(PriceInput):
    #This little function takes an integer or float as input and calculates the HST, the total with HST, formats both of those values (and the input value) to be receipt-ready, and returns all 5 values. This is designed to be used on value that has already been validated at an earlier step in the code.
    HST_RATE = 0.15
    HstAmt = PriceInput * HST_RATE
    TotalAmt = PriceInput + HstAmt
    PriceInputDSP = "${:,.2f}".format(PriceInput)
    HstAmtDsp = "${:,.2f}".format(HstAmt)
    TotalAmtDsp = "${:,.2f}".format(TotalAmt)
    #The values are returned as a tuple, an object that can be indexed like a list.
    return HstAmt, TotalAmt, PriceInputDSP, HstAmtDsp, TotalAmtDsp

def AnyKey(Prompt):
    #The following function advances the program after any key is pressed. First, end='' and flush=True are used to make the print function behave (keeping the cursor at the end of that line) Next, the code checks the operating system and then proceeds accordingly. In windows, the msvcrt.getch() function records the keystroke as a byte string, but doesn't produce anything in the console. In Unix systems (such as Linux or MacOS), the terminal is set to raw mode in the try statement,temporarilly (for one keystroke) preventing the character from appearing on the console. The finally statement brings the terminal back out of raw mode. This isn't the extra feature lol. I chose to import the modules within the function because it crashed the code for me otherwise.
    import sys
    print(Prompt, end='', flush=True)
    if sys.platform.startswith('win'):
        import msvcrt
        msvcrt.getch()
    else:
        import tty
        import termios
        FileDesc = sys.stdin.fileno()
        OldSettings = termios.tcgetattr(FileDesc)
        try:
            tty.setraw(FileDesc)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(FileDesc, termios.TCSADRAIN, OldSettings)
            
def Whoops(Prompt):
    #This function is a little escape hatch to allow the users to get out of a program without running it. Example use:
    # Main program
    #while True:
        #if not Whoops("If you accidentally chose Option 1,\ntype END and press return to go back to the main menu.\nOtherwise, press return to continue: "):
            #break
    print(Prompt, end='', flush=True)
    Oops = input().upper()
    print()
    if Oops == "END":
        return False
    else:
        return True

def Padding(string):
    #Adds blank lines before and after print statement
    print()
    print(string)
    print()

def NotBlank(Prompt):
    #Just a little function to make sure a field isn't blank. This is incorporated in several functions in this library.
    while True:
        UserInput = input(Prompt)
        if not UserInput:
            Padding("Error: Field cannot be blank.")
            continue
        else:
            return UserInput
        
def ValidNameAdd(Prompt):
    #Makes sure field isn't blank and formats cities to my preference
    import string
    while True:
        UserInput = NotBlank(Prompt)
        if not UserInput:
            continue
        else:
            return string.capwords(UserInput) + ",", UserInput.title()
            
            
def MoneyFloat(Prompt):
    #This function uses regex to ensure that a number is not only a float, but has no more than the two decimal places expected for a monetary value. There were fewer monetary inputs than expected, but we're proud of this and it will definitely be recycled in future code.
    import re
    pattern = r'^\d+(\.\d{1,2})?$'
    while True:
        UserFloat = NotBlank(Prompt)
        if not UserFloat:
            continue
        elif not re.match(pattern, UserFloat):
            Padding("Error: Please double check your value.")
        else:
            return float(UserFloat), "${:,.2f}".format(float(UserFloat))
        
def ValidPhone(Prompt):
    #This functions validates phone numbers to suit my preferred input format.
    while True:
        PhoneNum = NotBlank(Prompt)
        if not PhoneNum:
            continue
        elif len(PhoneNum) != 10:
            Padding("Error: Phone number must be 10 digits.")
        elif not PhoneNum.isdigit():
            Padding("Error: Phone number must be digits only.")
        else:
            return PhoneNum, f"({PhoneNum[0:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]}"

def ValidPost(Prompt):
    #This functions validates postal codes to suit my preferred input format.
    while True:
        PostCode = NotBlank(Prompt)
        if not PostCode:
            continue
        elif len(PostCode) != 6 or not PostCode[0].isalpha() or not PostCode[2].isalpha() or not PostCode[4].isalpha() or not PostCode[1].isdigit() or not PostCode[3].isdigit() or not PostCode[5].isdigit():
            Padding("Error: Invalid postal code.")
        else:
            return PostCode.upper(), f"{PostCode[0:3]} {PostCode[3:]}".upper()
    
def ValidProv(Prompt):
    #This functions validates province abbreviations to suit my preferred input format.
    while True:
        ProvList = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
        Province = NotBlank(Prompt).upper()
        if len(Province) != 2:
            Padding("Error: Province must be two characters (XX).")
        elif not Province.isalpha():
            Padding("Error: Province must be two letters (XX).")
        elif Province == "PQ":
            Province = "QC"
            return Province
        elif Province == "NF":
            Province = "NL"
            return Province
        elif Province not in ProvList:
            Padding(f"Error: Value not recognized as Canadian Province.\n{ProvList}")
        else:
            return Province

def ValidPlate(Prompt):
    #This functions validates licence plates to suit my preferred input format.
    while True:
        PlateNum = NotBlank(Prompt)
        if len(PlateNum) != 6:
            Padding("Error: Plate number must be six characters.")
        elif not PlateNum[0:3].isalpha() or not PlateNum[3:].isdigit():
            Padding("Error: Plate number must be three letters followed by three numbers.")
        else:
            return PlateNum.upper(), f"{PlateNum[0:3]} {PlateNum[3:]}".upper()

def AnimeScroll(Emoji = "(づ｡◕‿‿◕｡)づ", Phrase = "Mo is Tiggety-Boo!"):
    #I wanted to learn something new (the animation) while reviewing the append function for lists. The values defined are placeholders, another cool option would be calling AnimeScroll(input("Enter any ASCII emoji you want: "), input("Enter any phrase you want to appear with the emoji: ")) to allow user input.
    import time
    Frames = []
    Counter = 0
    PhraseCounter = 0
    while Counter < 3:
        Emoji = " " + Emoji
        Frames.append(Emoji)
        Counter += 1
    while 3 <= Counter <= (len(Phrase) + len(Emoji)):
        Frames.append(Phrase[0:PhraseCounter] + Emoji)
        Counter += 1
        PhraseCounter += 1
    for frame in Frames:
        print("\r" + frame, end="")
        time.sleep(0.1)
        
def ValidInt(Prompt):
    #Use example:
    #MyNum = ValidInt("Number?: ")
    #print(MyNum)
    while True:
        UserInput = NotBlank(Prompt)
        try:
            return int(UserInput) 
        except:
            Padding("Error: Value must be a whole number.")
            continue

def ValidFloat(Prompt):
    #Use example:
    #MyFloat = ValidFloat("Number?: ")
    #print(MyFloat)
    while True:
        UserInput = NotBlank(Prompt)
        try:
            float(UserInput)
            return UserInput, "${:,.2f}".format(UserInput)
        except:
            Padding("Error: Value must be a number.")
            continue
            
def ValidYN(Prompt, Choice1 = 'Y', Choice2 = 'N', *args):
    #Makes sure user only enters Y or N (or specifications if different is required)
    while True:
        UserInput = NotBlank(Prompt).upper()
        if UserInput != Choice1 and UserInput != Choice2 and UserInput not in args:
            if not args:
                Padding(f"Error: Value must be {Choice1} or {Choice2}.")
                continue
            else:
                Padding(f"Error: Value must be {Choice1} or {Choice2} or {' '.join(map(str, args))}.")
                continue
        else:
            return UserInput
            
def ValiDate(Prompt):
    #Returns a date as a string and an object in my preferred format
    from datetime import datetime
    AnyKey(Prompt)
    while True:
        Year = NotBlank("\nPlease enter the year (####): ")
        if not Year.isdigit() or len(Year) != 4:
            Padding("Error: Year must be four digits (####).")
            continue
        else:
            break
    while True:
        Month = ValidInt("Please enter the month (1-12): ")
        if not (1 <= Month <= 12):
            Padding("Error: Month needs to be a number from 1 to 12.")
            continue
        else:
            break
    while True:
        Day = ValidInt("Please enter the day (1-31): ")
        try:
            Date = datetime.strptime(f"{Year}-{Month}-{Day}", "%Y-%m-%d").date()
            return Date, f"{Year}-{Month}-{Day}"
        except:
            Padding("Error: Invalid date.")
            continue

def IntMoreZero(Prompt):
    #Checks to see if an integer is > 0
    while True:
        Num = ValidInt(Prompt)
        if Num <= 0:
            Padding("Error: Number cannot be 0 or less.")
            continue
        else:
            return Num

def FloatMoreZero(Prompt):
    #Checks to see if a float is > 0
    while True:
        Num = ValidFloat(Prompt)[0]
        if Num <= 0:
            Padding("Error: Number cannot be 0 or less.")
            continue
        else:
            return Num

def MFMoreZero(Prompt):
    #Checks to see if dollar value is > 0
    while True:
        Num = MoneyFloat(Prompt)[0]
        if Num <= 0:
            Padding("Error: Number cannot be 0 or less.")
            continue
        else:
            return Num
        
def FrstNxtMnth():
    import datetime
    if datetime.datetime.now().month < 12:
        next_month_year = datetime.datetime.now().year
    else:
        next_month_year = datetime.datetime.now().year + 1
    if datetime.datetime.now().month < 12:
        next_month = datetime.datetime.now().month + 1
    else:
        next_month = 1
    return datetime.datetime(next_month_year, next_month, 1), datetime.datetime(next_month_year, next_month, 1).strftime("%Y-%m-%d")

def UpdateFrstLn(Filename, NewValue):
    f = open(Filename, 'r')
    lines = f.readlines()
    lines[0] = NewValue + '\n'
    f = open(Filename, 'w')
    f.writelines(lines)
    f.close()

def ValidEmail(Prompt):
    import re
    EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    while True:
        Email = NotBlank(Prompt)
        if not EMAIL_REGEX.match(Email):
            Padding("Error: Invalid format for an email address.")
            continue
        else:
            return Email
