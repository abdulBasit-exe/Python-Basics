# 8.1
# def display_messege():
#     print('I\'m learning python!')

# display_messege()


# # 8.2
# def fav_book(title):
#     print("One of my fav book is "+title+".")


# fav_book('azadi')

# # 8.3
# def make_tshirt(size='large', messege='i love pyhton'):
#     print("Shirt is being made of "+str(size)+' size')
#     print("Messege on shirt will be: "+messege)

# make_tshirt(messege='i love java')


# # 8.4 
# def describe_city(city='karachi', country='pakistan', pop=' 100'):
#     print(city.title()+' is in '+country.title()+pop)

# describe_city(city='delhi',country='india')

# # 8.6
# def city_countries(city, country):
#     city=input()
#     country=input()
#     print('\"'+city.title()+", "+country.title()+"\"")


# city_countries('','')

# 8.7
# def make_album(artist,title):
#     album1={
#         'artist':input("Enter artist 1 name:"+artist),
#         'title':input("Enter title of album: "+title)
#     }
#     album2={
#         'artist':input("Enter artist 2 name:"+artist),
#         'title':input("Enter title of album: "+title)
#     }
#     album3={
#         'artist':input("Enter artist 3 name:"+artist),
#         'title':input("Enter title of album: "+title)
#     }
    

#     return album1, album2, album3

# print(make_album('',''))

# 8.9 
magicians= ['basit', 'uzair', 'sachal', 'monii']

def show_great_magician(magician):
    great_magicians=[]
    for name in magicians:
    #  print("we will see performance of "+name)
    # 8.10
    # print("The greatest of all time "+name.title())
        great_magicians.append("Great magician "+name.title())
    return great_magicians
    

print(show_great_magician(magician=magicians))