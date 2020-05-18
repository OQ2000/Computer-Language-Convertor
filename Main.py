import os
clear = lambda: os.system('cls')
clear()

def checkValidNumber(num):
    try:
        num = int(num)
    except:
        return(False,num)
    if num == 0:
        return(False,num)
    else:
        return(True,num)

def decimal2binary():
    UserEnteredNumber = 0
    Valid = False
    Binary = []
    while Valid == False:
        UserEnteredNumber = input("Please Enter A Number: ")
        Valid,UserEnteredNumber = checkValidNumber(UserEnteredNumber)
    while UserEnteredNumber != 0:
        tmpBin = UserEnteredNumber % 2
        Binary.append(tmpBin)
        UserEnteredNumber = int(UserEnteredNumber / 2)
    Binary.reverse()
    print("Your Number In Binary Is:","".join(str(v) for v in Binary))

def decimal2hex():
    Hex = {
        0 : 0,
        1 : 1,
        2 : 2,
        3 : 3,
        4 : 4,
        5 : 5,
        6 : 6,
        7 : 7,
        8 : 8,
        9 : 9,
        10 : 10,
        11 : "B",
        12 : "C",
        13 : "D",
        14 : "E",
        15 : "F"
    }
    UserEnteredNumber = 0
    Valid = False
    Binary = []
    while Valid == False:
        UserEnteredNumber = input("Please Enter A Number: ")
        Valid,UserEnteredNumber = checkValidNumber(UserEnteredNumber)
    while UserEnteredNumber != 0:
        tmpBin = UserEnteredNumber % 16
        tmpBin = Hex[tmpBin]
        Binary.append(tmpBin)
        UserEnteredNumber = int(UserEnteredNumber / 16)
    Binary.reverse()
    print("Your Number In Hex Is:","".join(str(v) for v in Binary))

def binary2decimal():
    UserEnteredNumber = 0
    Valid = False
    Binary = []   
    totalDecimal = 0
    while Valid == False:
        UserEnteredNumber = input("Please Enter Your Binary Number: ")
        Valid,UserEnteredNumber = checkValidNumber(UserEnteredNumber)
    strUserEnteredNumber = str(UserEnteredNumber)[::-1]
    # strUserEnteredNumber = strUserEnteredNumber[::-1]
    for i in range(len(str(UserEnteredNumber))):
        tmpLetter = str(strUserEnteredNumber[i])
        if tmpLetter == "0":
            pass
        else:
            tmpNum = int(math.pow(2,i))
            Binary.append(tmpNum)
 
    for i in range(len(Binary)):
        totalDecimal = totalDecimal + Binary[i]
    print("Your Number In Decimal Is:",totalDecimal)

def options():
    Valid = False
    Valid2 = False
    optionsList = ["decimal2binary","decimal2hex","binary2decimal"]
    clear()
    print("-------------------------------------")
    print("Please select an option from the list below that you would like to use:")
    print("Input the number you would like to use")
    print("Num :   Name of conversion")
    
    while Valid2 == False:
        while Valid == False:
            for i in range(len(optionsList)):
                    print(" ",i,":  ",optionsList[i])
            usrOption = input("Selection: ")
            try:
                usrOption = int(usrOption)
                Valid = True
            except:
                clear()
                print("Please Select A Valid Function")
        try:
            tmpOption = optionsList[usrOption]
            Valid2 = True
        except:
            clear()
            print("Please Select A Valid Function")
            Valid = False
    methodtocall = globals()[tmpOption]
    methodtocall()
   

options()

