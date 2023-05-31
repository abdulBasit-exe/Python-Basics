# age = int(input("whats your age? "))

# if age<18: print("you are below 18")
# elif age>18 : print("you are above 18")
# else: print("you are 18")


def compare(num1, num2, num3):
    if num1>=num2 and num2>=num3: 
        print(str(num1)+" is the biggest")
    elif num2>=num1 and num2>=num3:
        print(str(num2)+" is the biggest")
    elif num3>=num1 and num3>=num2:
        print(str(num3)+" is the biggest")
    else: print("all are equal")

compare(1,2,3)