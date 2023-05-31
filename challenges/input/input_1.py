# 7.1
# name = input('Enter your name: ')
# car = input("Enter the car you want: ")
# print('Sure '+name.title()+', let me see a '+car.title()+" for you!")

# 7.2

# people = input('How many poeple you are? ')
# people= int(people)
# if people>8 : print("You'll have to wait then!")
# else : print("Sure dear, just wait for 5 mins.")

# 7-3
# num = input('Enter any number: ')
# num= int(num)
# if num%10==0: print('This number is multiple of 10.')
# else: print('number is not multiple of 10')

# 7-4 
# flag = True
# pizza_toppings = []

# while flag:
#     topping = input("Enter a pizza topping (enter 'quit' to exit): ")
#     if topping.lower() == 'quit':
#         flag = False
#     else:
#         pizza_toppings.append(topping)
#         print("Adding", topping, "to your pizza.")

# print("Your pizza toppings are:", pizza_toppings)

# 7.8 

# sandwiches = ['double cheese', 'cheese', 'mustard', 'chilly']
# finished_sandwich=[]

# for current in sandwiches:
#     print("I made your "+current.title())
#     finished_sandwich.append(current)

# print("These sandwiches were made: ", finished_sandwich)


# 7.9
sandwiches = ['double cheese','pastrami', 'cheese', 'pastrami', 'mustard','pastrami', 'chilly']
finished_sandwich=[]

print('We are out of pastrami')

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami') 
for current in sandwiches:
    
    print("I made your "+current.title())
    finished_sandwich.append(current)

print("These sandwiches were made: ", finished_sandwich)

