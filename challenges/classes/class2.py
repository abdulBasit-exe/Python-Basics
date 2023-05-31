# # 9.3
# class User():
#     user_attempt=0


#     def increment_user_input(self):
#         self.user_attempt+=1
#         return self.user_attempt
    
#     def reset_user_input(self):
#         self.user_attempt=0
#         return self.user_attempt
    
#     def __init__(self, name , id , tweets, rts, followers) :
#         self.name= name
#         self.id = id
#         self.tweets= tweets
#         self.rts = rts
#         self.followers = followers
    
#     def describe_user(self):
#         print('Name: '+self.name)
#         print('\nID: '+str(self.id))
#         print('Tweets: '+str(self.tweets))
#         print('RTs: '+str(self.rts))
#         print('Followers: '+str(self.followers))
    
#     def greet_user(self):
#         print("Welcome to the online forum "+self.name)


# user1= User('basit',91,10,1,2)
# print(user1.user_attempt)
# user1.increment_user_input()
# user1.increment_user_input()
# user1.increment_user_input()
# user1.increment_user_input()
# print(user1.user_attempt)
# user1.reset_user_input()
# print(user1.user_attempt)

# basit = User('basit',91, 10023, 980, 690)
# basit.describe_user()

# # 9.4

class Restraunt():
    def __init__(self, restraunt_name,number_saved=0,cuisine='chinese') :
        self.restraunt_name = restraunt_name
        self.cuisine = cuisine
    
    def describe_restraunt(self):
        print(self.restraunt_name+" is the restraunt name and its cuisine is "+self.cuisine)

    def open_restraunt(self):
        print(self.restraunt_name+' is open!')
    def increase_served(self, served):
        self.number_served=served
        return self.number_served
    
rest = Restraunt('rt')

print(rest.increase_served(100))
# print(rest.increase_served(100))

    
# 9.6
class IceCreamStand(Restraunt):
    flavors =[]
    def __init__(self, restraunt_name,  flavors ,number_saved=0, cuisine='chinese'):
        super().__init__(restraunt_name, flavors,cuisine='ice-cream')
        for flavor in flavors:
            self.flavors=flavor
    
    def describe_restraunt(self, flavors):
        for flavor in flavors:
            print(flavor)
        

flavors=['mango','lichi', 'choco']
walls = IceCreamStand('rt',flavors)
walls.describe_restraunt(flavors)