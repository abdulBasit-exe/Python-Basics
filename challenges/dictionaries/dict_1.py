# # # 6.1 person
# # person_info = {
# #     'f_name': 'basit',
# #     'l_name': 'memon',
# #     'age':'19',
# #     'city':'sukkur'
# # }
# # print(person_info['f_name'])
# # print(person_info['l_name'])
# # print(person_info['age'])
# # print(person_info['city'])

# # 6.2 Fav Number
# fav_num={
#     'basit':input("Enter your fav Number ".title()),
#     'uzair':input("Enter your fav Number"),
#     'sachal':input("Enter your fav Number"),
#     'monii':input("Enter your fav Number"),
#     'mama mir':input("Enter your fav Number"),
# }

# print("Fav numbers of people: ")
# print("basit: "+fav_num['basit'])
# print("uzair: "+fav_num['uzair'])
# print("sachal: "+fav_num['sachal'])
# print("monii: "+fav_num['monii'])
# print("mama mir: "+fav_num['mama mir'])

# looping through the dictionary

# for key, value in fav_num.items():
#     print(key.title()+" : "+value.title())

# only the keys

# for key in fav_num.keys():
#     print(key.title())

# # sorted 
# for key in sorted(fav_num):
#     print(key.title())

# set function to omit the duplicate values.
# for num in set(fav_num.values()):
#     print(num)

# 6.5 River 
# river ={
#     'Indus River':"Sindh",
#     'Satlaj':"Punjab",
#     'Nile':"Egypt",
#     'Amazon':"south africa",
#     'Congo':"zambia",
# }

# for key, value in river.items():
#     print(key.title()+" runs in "+value.title())

# for river in river.keys():
#     print(river)


# for river in river.values():
#     print(river)

# people_details = [
#     {
#         'name':'basit',
#         'age':'19',
#         'city':'sukkur',
#         'dept': 'sw'
#     }
#     ,
#     {
#         'name':'sachal',
#         'age':'20',
#         'city':'ranipur',
#         'dept': 'cs'
#     }
# ]

# for people in people_details:
#     for key, value in people.items():
#         print(key.title()+":\t"+value.title())
#     print('')


# 6.8

# cat = {
#     'name': 'jack',
#     'owner': 'unknown',
#     'color':'black',
#     'age': '2yrs'
# }

# dog = {
#     'name': 'husky',
#     'owner': 'basit',
#     'color':'white',
#     'age': '3yrs'
# }
# parrot = {
#     'name': 'mitho',
#     'owner': 'sachal',
#     'color':'green',
#     'age': '0.5 yrs'
# }

# pigoen = {
#     'name': 'musky',
#     'owner': 'uzair',
#     'color':'grey',
#     'age': '1yr'
# }

# pets=[cat,dog,pigoen,parrot]

# for pet in pets:
#     for key,value in pet.items():
#         print(key.title()+":\t"+value.title())
#     print()


# 6.8 Fav place
# fav_places={
#     'basit':'mithi',
#     'uzair':'rohri',
#     'sachal':'karoonjhar',
#     'khaliq':input("Whats your fav place?"),
#     'monii':input("Whats your fav place?"),
#     'sumair':input("Whats your fav place?"),
# }

# for key,value in fav_places.items():
#     print(key.title()+"'s fav place is : "+value.title())

# 6.11

# cities={
#     'karachi':{
#         'province':'sindh',
#         'population':'22million',
#         'fact':'snatching'
#     },
#     'lahore':{
#         'province':'punjab',
#         'population':'15million',
#         'fact':'beef is not beef!'
#     },
#     'quetta':{
#         'province':'balochistan',
#         'population':'5million',
#         'fact':'best for car\'s engine'

#     }
# }

# for key_city,val_cities in cities.items():
#     print(key_city.title())
#     for key_info, val_info in val_cities.items() :
#         print(key_info.title()+': '+val_info.title())
#     print()

    
import subprocess

def convert_video_to_mp3(video_url):
    # Download the video using youtube-dl
    subprocess.call(['youtube-dl', '--extract-audio', '--audio-format', 'mp3', video_url])

# Example usage:
video_url = 'https://youtu.be/hfL9V1PLMjs'
convert_video_to_mp3(video_url)
