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

