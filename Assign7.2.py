def isValid(password):
  
    # for checking if password length
    # is greater than 15
    if (len(password) < 15):
        return False
  
    # to check space
    if (" " in password):
        return False
  
    if (True):
        count = 0
  
        # check digits from 0 to 9
        arr = ['0', '1', '2', '3', 
        '4', '5', '6', '7', '8', '9']
  
        for i in password:
            if i in arr:
                count = 1
                break
  
        if count == 0:
            return False
  
    # for special characters
    if True:
        count = 0
  
        arr = ['@', '#','!','~','$','%','^',
                '&','*','(',',','-','+','/',
                ':','.',',','<','>','?','|']
  
        for i in password:
            if i in arr:
                count = 1
                break
        if count == 0:
            return False
  
    if True:
        count = 0
  
        # checking capital letters
        for i in range(65, 91):
  
            if chr(i) in password:
                count = 1
  
        if (count == 0):
            return False
  
    if (True):
        count = 0
  
        # checking small letters
        for i in range(90, 123):
  
            if chr(i) in password:
                count = 1
  
        if (count == 0):
            return False
  
    # if all conditions fails
    return True

password1 =input("your password:") 
  
if (isValid([i for i in password1])):
    print("Valid Password")
else:
    print("Invalid Password!!!")