# # 5.3 Alien Color -1 
# alien_color = 'yellow'
# aliean =10
# if alien_color== 'blue' :
#     print('U didnt earned anything!')
# elif alien_color=='red':
#     print('U earned 10$')
# elif alien_color== 'green':
#     print('U earned 5$')

# # 5.8 and  5.9
# # users = ['jack', 'shawn', 'mike', 'admin', 'paul']
# users = []

# # if len(users) != 0:
# #         for user in users:
# #             if user != 'admin':
# #                 print("Welcome again "+user+" thankyou for logging again!")
# #             elif user == 'admin':
# #                 print("Hello Admin! ")
# # else: print("list is empty!")

# # 5.10 
# existing_users = ['basit', 'uzair', 'sachal', 'sumair', 'monii']
# new_users=['moni','wahab', 'basit', 'ashish', 'faraz']

# for check in new_users:
#     if check in existing_users:
#             print(check+" already exist!, kindly enter your name again")
#     else : print('username available!')

# 5.11 Ordinal numbers 

nums = [i for i in range(1,10)]

for num in nums:
    if num == 1:
        print(str(num)+"st")
    elif num == 2:
        print(str(num)+"nd")
    elif num == 3:
        print(str(num)+"rd")
    else: print(str(num)+"th")
