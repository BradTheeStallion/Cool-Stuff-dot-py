#Nifty Functions
#By Brad Ayers
#February 2024 - Present

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

def FloatTest(prompt):
    #This function uses regex to ensure that a number is not only a float, but has no more than the two decimal places expected for a monetary value. There were fewer monetary inputs than expected, but we're proud of this and it will definitely be recycled in future code.
    import re
    pattern = r'^\d+(\.\d{1,2})?$'
    while True:
        UserFloat = input(prompt)
        if not UserFloat:
            print()
            print("Error: cannot be blank.")
            print()
        elif not re.match(pattern, UserFloat):
            print()
            print("Error: Please double check your value.")
            print()
        else:
            return float(UserFloat)
        
def ValidPhone(prompt):
    #This functions validates phone numbers to suit my preferred input format.
    while True:
        PhoneNum = input(prompt)
        if not PhoneNum:
            print("Error: Phone number cannot be blank.")
        elif len(PhoneNum) != 10:  
            print("Error: Phone number must be 10 digits.")
        elif not PhoneNum.isdigit(): 
            print("Error: Phone number must be digits only.")
        else:
            break

def ValidPost(prompt):
    #This functions validates postal codes to suit my preferred input format.
    while True:
        PostCode = input(prompt).upper()
        if not PostCode:
            print()
            print("Error: Postal code cannot be blank.")
            continue
        elif len(PostCode) != 6 or not PostCode[0].isalpha() or not PostCode[2].isalpha() or not PostCode[4].isalpha() or not PostCode[1].isdigit() or not PostCode[3].isdigit() or not PostCode[5].isdigit():
            print()
            print("Error: Invalid postal code.")
            continue
        else:
            break
    
def ValidProv(prompt):
    #This functions validates province abbreviations to suit my preferred input format.
    while True:
        Province = input(prompt).upper()
        if not Province:
            print()
            print("Error: Province cannot be blank.")
            continue
        elif len(Province) != 2:
            print()
            print("Error: Province must be two characters (XX).")
            continue
        elif not Province.isalpha():
            print()
            print("Error: Province must be two letters (XX).")
        else:
            break

def ValidPlate(prompt):
    #This functions validates licence plates to suit my preferred input format.
    while True:
        PlateNum = input(prompt).upper()
        if not PlateNum:
            print()
            print("Error: Customer plate number cannot be blank.")
            continue
        elif len(PlateNum) != 6:
            print()
            print("Error: Customer plate number must be six characters.")
            continue
        elif not PlateNum[0:3].isalpha() or not PlateNum[3:].isdigit():
            print()
            print("Error: Customer plate number must be three letters followed by three numbers.")
            continue
        else:
            break