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

def AnyKey(prompt):
    #The following function advances the program after any key is pressed. First, end='' and flush=True are used to make the print function behave (keeping the cursor at the end of that line) Next, the code checks the operating system and then proceeds accordingly. In windows, the msvcrt.getch() function records the keystroke as a byte string, but doesn't produce anything in the console. In Unix systems (such as Linux or MacOS), the terminal is set to raw mode in the try statement,temporarilly (for one keystroke) preventing the character from appearing on the console. The finally statement brings the terminal back out of raw mode. This isn't the extra feature lol. I chose to import the modules within the function because it crashed the code for me otherwise.
    import sys
    print(prompt, end='', flush=True)
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
            
def Whoops(prompt):
    #This function is a little escape hatch to allow the users to get out of a program without running it. Example use:
    # Main program
    #while True:
        #if not Whoops("If you accidentally chose Option 1,\ntype END and press return to go back to the main menu.\nOtherwise, press return to continue: "):
            #break
    print(prompt, end='', flush=True)
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

def NotBlank(UserInput):
    #Just a little function to make sure a field isn't blank. This is incorporated in several functions in this library.
        if not UserInput:
            Padding("Error: Field cannot be blank.")
            return False
        else:
            return UserInput

def ValidNameAdd(prompt):
    #Makes sure field isn't blank and formats names and cities to my preference
    import string
    while True:
        UserInput = NotBlank(input(prompt))
        if not UserInput:
            continue
        else:
            return string.capwords(UserInput), UserInput.title

def MoneyFloat(prompt):
    #This function uses regex to ensure that a number is not only a float, but has no more than the two decimal places expected for a monetary value. There were fewer monetary inputs than expected, but we're proud of this and it will definitely be recycled in future code.
    import re
    pattern = r'^\d+(\.\d{1,2})?$'
    while True:
        UserFloat = NotBlank(input(prompt))
        if not UserFloat:
            continue
        elif not re.match(pattern, UserFloat):
            Padding("Error: Please double check your value.")
        else:
            return float(UserFloat), "${:,.2f}".format(float(UserFloat))
        
def ValidPhone(prompt):
    #This functions validates phone numbers to suit my preferred input format.
    while True:
        PhoneNum = NotBlank(input(prompt))
        if not PhoneNum:
            continue
        elif len(PhoneNum) != 10:
            Padding("Error: Phone number must be 10 digits.")
        elif not PhoneNum.isdigit():
            Padding("Error: Phone number must be digits only.")
        else:
            return PhoneNum, f"({PhoneNum[0:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]}"

def ValidPost(prompt):
    #This functions validates postal codes to suit my preferred input format.
    while True:
        PostCode = NotBlank(input(prompt).upper())
        if not PostCode:
            continue
        elif len(PostCode) != 6 or not PostCode[0].isalpha() or not PostCode[2].isalpha() or not PostCode[4].isalpha() or not PostCode[1].isdigit() or not PostCode[3].isdigit() or not PostCode[5].isdigit():
            Padding("Error: Invalid postal code.")
        else:
            return PostCode, f"{PostCode[0:3]} {PostCode[3:]}"
    
def ValidProv(prompt):
    #This functions validates province abbreviations to suit my preferred input format.
    while True:
        ProvList = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
        Province = NotBlank(input(prompt).upper())
        if not Province:
            continue
        elif len(Province) != 2:
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

def ValidPlate(prompt):
    #This functions validates licence plates to suit my preferred input format.
    while True:
        PlateNum = NotBlank(input(prompt).upper())
        if not PlateNum:
            continue
        elif len(PlateNum) != 6:
            Padding("Error: Plate number must be six characters.")
        elif not PlateNum[0:3].isalpha() or not PlateNum[3:].isdigit():
            Padding("Error: Plate number must be three letters followed by three numbers.")
        else:
            return PlateNum, f"{PlateNum[0:3]} {PlateNum[3:]}"

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
        
def ValidInt(prompt):
    #Use example:
    #MyNum = ValidInt("Number?: ")
    #print(MyNum)
    while True:
        UserInput = NotBlank(input(prompt))
        if not UserInput:
            continue
        else:
            try:
                int(UserInput)
                return UserInput 
            except:
                Padding("Error: Value must be a whole number.")
                continue

def ValidFloat(prompt):
    #Use example:
    #MyFloat = ValidFloat("Number?: ")
    #print(MyFloat)
    while True:
        UserInput = NotBlank(input(prompt))
        if not UserInput:
            continue
        else:
            try:
                float(UserInput)
                return UserInput, "${:,.2f}".format(UserInput)
            except:
                Padding("Error: Value must be a number.")
                continue
