class Restraunt():
    def __init__(self, restraunt_name, cuisine='chinese') :
        self.restraunt_name = restraunt_name
        self.cuisine = cuisine
    
    def describe_restraunt(self):
        print(self.restraunt_name+" is the restraunt name and its cuisine is "+self.cuisine)

    def open_restraunt(self):
        print(self.restraunt_name+' is open!')


my_restraunt = Restraunt("RT",'Pakistani')
print(my_restraunt.restraunt_name)
print(my_restraunt.cuisine)
my_restraunt.describe_restraunt()
my_restraunt.open_restraunt()

rest1 = Restraunt('sajjad', 'all variety')
rest2 = Restraunt('sindhri', 'desi')
rest3 = Restraunt('italian pizza', 'italian')

rest1.describe_restraunt()
rest2.describe_restraunt()
rest3.describe_restraunt()