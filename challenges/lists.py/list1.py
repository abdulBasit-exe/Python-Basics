# # list = ["this", "is ", "a ", "list", "in ","python"]

# # print(list[0].title()) #  -> This

# # # 3-1. Names: Store the names of a few of your friends in a list called names. Print
# # # each person’s name by accessing each element in the list, one at a time.

# # names = ["abdul khalique", "Uzair Qureshi", "Muzammil"]
# # # print(names[0])
# # # print(names[1])
# # # print(names[2])

# # # 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# # # printing each person’s name, print a message to them. The text of each message
# # # should be the same, but each message should be personalized with the
# # # person’s name.

# # print("Hello dear "+ names[0]+", Welcome to the club!")
# # print("Hello dear "+ names[1]+", Welcome to the club!")
# # print("Hello dear "+ names[2]+", Welcome to the club!")

# # print(names[0].title())

# # 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# # would you invite? Make a list that includes at least three people you’d like to
# # invite to dinner. Then use your list to print a message to each person, inviting
# # them to dinner.

names = ["basit", "uzair", "sachal"]
msg=", You are invited at the dinner!"

# for i in names:
#     print("Hello "+i+msg)

print("Dinner table is expanded!")

names.insert(0,"monii")
names.insert(len(names)//2,"khaliq")
names.insert(len(names),"summu")

# for i in names:
#      print("Hello "+i+msg)

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to

print("Dinner table can't be booked!")

for i in range(2):
    print("Sorry "+ names.pop()+", u can't be invited to the dinner!")


for i in names: 
    print(i+", You are invited!")

# del names[:]

print(sorted(names, reverse=True))