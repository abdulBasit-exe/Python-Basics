class User():
    user_attempt=0


    def increment_user_input(self):
        self.user_attempt+=1
        return self.user_attempt
    
    def reset_user_input(self):
        self.user_attempt=0
        return self.user_attempt
    
    def __init__(self, name , id , tweets, rts, followers) :
        self.name= name
        self.id = id
        self.tweets= tweets
        self.rts = rts
        self.followers = followers
    
    def describe_user(self):
        print('Name: '+self.name)
        print('\nID: '+str(self.id))
        print('Tweets: '+str(self.tweets))
        print('RTs: '+str(self.rts))
        print('Followers: '+str(self.followers))
    
    def greet_user(self):
        print("Welcome to the online forum "+self.name)


user1= User('basit',91,10,1,2)
print(user1.user_attempt)
user1.increment_user_input()
user1.increment_user_input()
user1.increment_user_input()
user1.increment_user_input()
print(user1.user_attempt)
user1.reset_user_input()
print(user1.user_attempt)

basit = User('basit',91, 10023, 980, 690)
basit.describe_user()

# 9.7

class Admin(User):
    def __init__(self, name, id, tweets, rts, followers):
        super().__init__(name, id, tweets, rts, followers)
        self.privilages = ['can add a user', 'can update panel', 'can delete a user']

    def showPrivilages(self):
        print(f"Admin Privilages: {','.join(self.privilages)}")
    

admin1 = Admin('basit',91,20,11,100)
admin1.showPrivilages()