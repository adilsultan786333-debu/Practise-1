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


#answer 1
def reverse_recursive(num):
    if num == "":
        return num
    else:
        return num[-1] + reverse_recursive(num[:-1])   

num = input("Enter a number: ")

rev = reverse_recursive(num)

print("Reversed Number:", rev)

if num == rev:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")

#answer2

def outer_function(a, b):
 
    def inner_function():
        return a + b  

    total = inner_function()  
    total = total + 5          
    return total   
           
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

answer = outer_function(num1, num2)
print("Final Result =", answer)

#answer 4
year = int(input("Enter a year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("{year} is a Leap Year.")
        else:
            print(f"{year} is NOT a Leap Year.")
    else:
        print("{year} is a Leap Year.")
else:
    print("{year} is NOT a Leap Year.")

#answer 3
def sum_numbers(n):
    
    if n == 0:
        return 0
    
    return n + sum_numbers(n - 1)

result = sum_numbers(10)
print( result)
#gvuzcxbjcxg

choice = int(input("Enter choice (1-4): "))

match choice:
    case 1:
        n = int(input("Enter N: "))
        for i in range(2, n+1, 2):
            print(i, end=" ")

    case 2:
        n = int(input("Enter N: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)

    case 3:
        op = int(input("Enter operation (1-div, 2-avg, 3-power, 4-percentage): "))
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        match op:
            case 1:
                print("Division =", a / b)
            case 2:
                print("Average =", (a + b) / 2)
            case 3:
                print("Power =", a ** b)
            case 4:
                print("Percentage =", (a / b) * 100)
            case _:
                print("Invalid operation")

    case 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))

        if a >= b and a >= c:
            print("Largest =", a)
        elif b >= a and b >= c:
            print("Largest =", b)
        else:
            print("Largest =", c)

    case _:
        print("Invalid choice")

#task 2
fruits = ["apple", "banana", "mango", "orange"]
fruits[3]="grapes"
print(fruits)

fruits = ["apple", "banana", "mango", "orange"]
fruits[3]="grapes"
fruits.remove("banana")

fruits = ["apple", "banana", "mango", "orange"]
fruits.pop(3)
print(fruits)

fruits = ["apple", "banana", "mango", "orange"]
fruits.insert(1,"kiwi")
print(fruits)

fruits = ["apple", "banana", "mango", "orange"]
fruits.sort()
print(fruits)

fruits = ["apple", "banana", "mango", "orange"]
print(fruits[1:4])

#calendar
a=35
b=55
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#casting
x='565'
print(type(x))
print(type(int(x)))

#resuit grade
mark=50
if mark>=90:
    print("grade A")
elif mark>=80:
    print("Grade B")
elif mark>=70:
    print("Grade C")
elif mark>=60:
    print("Grade d")
    
elif mark>=50:
    print("Grade e")
else:
    print("fail")
aa=55
marks = [65, 78, 45, 90, 56]
marked=list(marks)
marked.append(aa)
marks=tuple(marked)
print(marks)

numbers = [5, 2, 9, 1, 7]
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
print(ascending)
print(descending)

if mark>50:
    print("fail")
else:
    print("pass")
    

#Assisgment 
for i in range(1):
    num1 = int(input("first number enter karein: "))
    num2 = int(input("second number enter karein: "))
    operattor = input("sign choose karein (+, -, *, /): ")

    if operattor == "+":
        print("Result:", num1 + num2)
    elif operattor == "-":
        print("Result:", num1 - num2)
    elif operattor == "*":
        print("Result:", num1 * num2)
    elif operattor == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        
    else:
        print("wrong operator")

#gfhgdnas
for i in range(1,6):
    for j in range(1,i + 1):
        print(j, end="")
    print()
    
    #task 2
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

#task 3
for i in range(1, 6):
    for j in range(i):
        print("+", end=" ")
    print()
#task 4
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

#task 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ") 
    print()

#task 6
for i in range(1,8):
    for j in range(i):
     print("*",end="")
    print()

Introduction="My Self"
name="Adil"
F_Name="Sultan"
live="karchi"

print(Introduction,name,F_Name,live)

Add=656
Sum=458
Odd=549
Even=112

print(Add+Sum+Odd+Even)

#sweaping

a1=56
a2=85

aa=a1
a1=a2
a2=aa

print(a1)
print(a2)

sub1,sub2,sub3,sub4,sub5,sub6="Math","computer","English","Science","urdu","Islamiat"
print(sub1)
print(sub6)
print(sub1,sub2,sub3,sub4,sub5,sub6)
print(sub1,sub5)


x=35
print(type(x))
print(type(str(x)))
print(type(float(x)))
#task01

username="Adil"
Password=8080
if(username is "Adil" and Password is 8080):
    print("login sucessfuly")
else:
    print("No login")
    
#Task 02
Day=6
if Day ==1:
    print("Monday")
elif  Day==2:
    print("Tuesday")
elif  Day==3:
    print("Wednesday")
elif  Day  ==4:
    print("Thursday")
elif  Day  ==5:
    print("friday")
elif  Day  ==6:
    print("saturday")
elif  Day  ==7:
    print("sunday")
else:
    print ("invalid number")
    
    # Task  03
Age =19
if Age <=18:
         print("eligibale")
else:
    print("not eligable") 
    
#calculator of match and case
num1=int(input("inter your first number="))
num2=int(input("inter your second number="))
oprator=(input("operation(+,-,/,*)="))

match oprator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "/":
        print(num1/num2)
    case "*":
        print(num1*num2)
    case _:
        print("error") 

print("My Name Is Adil")
print("I Am 15 Year old")
print("My Favourite Color Is Blue")

name="Adil"
Age=15
city="karachi"
House="Abdullah Goth" 

print(name)

print(Age)

print(city)

print(House)


Namee="My Name Is Adil "
Aage="I am 15 Year Old"
place="and I Live In Abdullah Goth Bin Qasim Town karachi"

print(Namee,Aage,place)

a=100
b=40
print(a+b)
print(a-b)
print(a*b)
print(a/b)

school_name = "The Professional Educator"
class_name = "8th"
favorite_subject = "Math,Computer"

print(school_name)
print(class_name)
print(favorite_subject)
 
#sweeping

s1=9999
s2=522


aa=s1
s3=s2
s4=aa

print(s1)
print(s2)


##print(type(t))
w=14
e=w
z=e
print(w)
print(e)
print(z)

#casting
x=5.55
print(type(int(x)))
#casting

x='5655'

print(type(x))

print(type(int(x)))

f=16566
s=str(f)

print(type(s))

f=3.251
s=int(f)

print(type(s))
print(s)
##print(type(t))

x=90

yy=x

zz=yy

a=b=c=d=78

print(x)
print(yy)
print(zz)

g,h,i=12,"sir shahzad",15

print(g)
print(h)
print(i)
a=10000
s=23
z=a
a=s
s=z
print(a)
print(s)

# List of numbers
numbers = [10, 5, 23, 7, 15]

# Calculate operations
total_sum = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Print results
print("Numbers:", numbers)
print("Sum:", total_sum)
print("Maximum:", maximum)
print("Minimum:", minimum)



thislist = ["adil", "zohaib", "saeed"]
thislist[2] = "muzamil"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["adil", "zohaib", "arooba"]
tropical = ["adil", "zohaib", "saeed"]
thislist.extend(tropical)
print(thislist)


thislist = ["adil", "zohaib", "saeed"]
thislist.remove("saeed")
print(thislist)


thislist = ["adil", "zohaub", "saeed", "muzamil", "arooba"]
thislist.remove("arooba")
print(thislist)


thislist = ["adil", "zohaib", "saeed"]
thislist.pop(1)
print(thislist)



