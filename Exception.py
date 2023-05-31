try:
    num=int(input("Enter a number"))
    print(10/num)
except ZeroDivisionError as err:
     print(err)
except KeyError as key:
     print(key)
