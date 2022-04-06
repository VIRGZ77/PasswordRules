# PasswordCheck

def ERRLEN(password):
    if len(password) <= 8:
        return True
    return False

def ERRSPC(password):
    for c in password:
        if c.isspace():
            return True
    return False

def ERRPWD(password):
    if (password[0:8].upper() == "PASSWORD"):
        return True
    return False

def ERRUPR(password):
    for c in password:
        if c.isupper():
            return False
    return True

def ERRLWR(password):
    for c in password:
        if c.islower():
            return False
    return True

def ERRNUM(password):
    for c in password:
        if c.isdigit():
            return False
    return True


while True:
    InvalidPassword = False    
    password = input("Enter a new password: ")
    
    if ERRLEN(password):
        InvalidPassword = True
        
    if ERRSPC(password):
        InvalidPassword = True
        
    if ERRPWD(password):
        InvalidPassword = True
        
    if ERRUPR(password):
        InvalidPassword = True
        
    if ERRLWR(password):
        InvalidPassword = True
        
    if ERRNUM(password):
        InvalidPassword = True
    
    if not(InvalidPassword):
        print("Password Accepted")
        break
    
    print("Invalid Password")
