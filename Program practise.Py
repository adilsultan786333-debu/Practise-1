def pass_word():
    password = input("Enter a Password: ")

    upper = False
    lower = False
    digit = False
    special_character = False

    special_chars = "!@#$%^&*()-_=+[]|;:'\",.<>?/`~"

    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
        elif i in special_chars:
            special_character = True

    if len(password) < 8:
        print("Password must be at least 8 characters long")
    elif upper and lower and digit and special_character:
        print("Password is strong")
    elif upper and lower and digit:
        print("Password is medium")
    elif upper and lower:
        print("Password is weak")
    else:
        print("Password is not well")
pass_word()

######dcfcfcfd
def table_of_2(n):
    if n > 10:      
        return
    print(f"3 x {n} = {2*n}")
    table_of_2(n + 1)   

table_of_2(1)


#fcgsvx
def is_even(num):
    if(num/2==0):
        return "even number"
    is_odd(num)

def is_odd(num):
    if(num%2==1):
        return "ODD number"
    is_even(num)

print(is_even(274))
print(is_odd(123))


