def chasr(password):
    # Minimum length requirement
    if len(password) > 8:
        print("8+ characters ---> ✔")
        return "true"
    else:
        print("8+ characters ---> X" )
        return "false"
def uppercase(password):
    if not any(char.isupper() for char in password):
        print("uppercase -------> X")
        return "false"
    else:
        print("Uppercase -------> ✔")
        return "true"
def lowercase(password):
    if not any(char.islower() for char in password):
        print("lowercase -------> X")
        return "false"
    else:
        print("lowercase -------> ✔")
        return "true"
def digi(password):
    if not any(char.isdigit() for char in password):
        print("digits ----------> X")
        return "false"
    else:
        print("Digits ----------> ✔")
        return "true"
def special(password):
     if not any(char in special_chars for char in password):
        print("symbol ----------> X")
        return "false"
     else:
        print("symbols ---------> ✔")
        return "true"

while True:
    print(" 1. check (y/n) \n 2. close(y/n) ")
    a = input("enter your choice:")

    if a=="y" or a=="1":
        password = input("enter password => ")
        print("password = ",password)
        special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
        
        for i in range(0,1):
            
            # Minimum length requirement
            character=chasr(password)
            
             # Check for uppercase letters
            uppercases=uppercase(password)
            
            # Check for lowercase letters
            lowercases=lowercase(password)
            
             # Check for digits
            digits=digi(password)
            
            # Check for special characters
            symbols=special(password)
            
        if character== "true" and uppercases=="true" and digits=="true" and symbols=="true":
            print("//////////strong///////////")
        else:
            print("///////////not strong///////////")
        print("------------------------------------")
        
    elif a=="n" or a=="2":
        break
    else:
        print("enter valid choice")
        
