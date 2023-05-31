# - 4.1 Pizza
pizza = ['chicken tikka', 'fajita', 'shawarma']

for flavor in pizza: 
    print("I like to have "+flavor.title())

print("In short, i like pizza alot!")

# 4.2 Animals

# animals = ['cat', 'dog', 'mouse']

# for animal in animals:
#     print(animal.title()+" would be a good option for pet!")

# print('any of them would be a fun to have as a pet! ')

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.

# numbers = [i for i in range (1,100)]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# #- 4.6 ODDS
# odd = [odds for odds in range(1,20,2)]
# print(odd)

# # 4.7 Multiples of three
# three = [threes for threes in range(3,31,3)]
# print(three)

# 4.8 Cube 
# cube = [cubes**3 for cubes in range(1,11)]
# for cubes in cube:
#     print(cubes)


# 4.10 Slices
# print('the first three cubes are: ')
# print(cube[:3])
# print('the three cubes from middle are: ')
# print(cube[3:6])
# print('the three cubes from end are')
# print(cube[7:])

friends_pizza = pizza[:]
pizza.append("pepperoni")
friends_pizza.append("malae tikka")
print('my pizzas: '+str(pizza))
print('my friend\'s pizzas: '+str(friends_pizza))