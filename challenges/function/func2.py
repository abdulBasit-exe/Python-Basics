# # 8.12
# def make_sandwich(*items):
#     print('The sandwich contains following items: ')
#     for item in items:
#         print(item)

# make_sandwich('bread','cheese', 'mushrooms', 'chicken\n')
# make_sandwich('bread','mayo\n')
# make_sandwich('bread','cheese', 'mushrooms', 'chicken', 'shrimps', 'ketchup\n')

# def make_profile(first_name, last_name, **details):
#     profile={}
#     profile['first name']= first_name
#     profile['last name']=last_name
#     for key, value in details.items():
#         profile[key] = value
#     return profile


# basit_profile=make_profile('basit', 'memon', city='Sukkur', dept='SWE', batch='2021', uni='Muet')
# print(basit_profile)

# # 8.14 
# def car_info(manufacturer, model_name, **info):
#     detail={}
#     detail['manufacturer']= manufacturer
#     detail['model_name']= model_name

#     for key, value in info.items():
#         detail[key]=value
#     return detail

# corolla = car_info('toyota', 'corolla 2014', color='white', cc=1800, variant='grande')
# print(corolla)

from function import show_great_magician as magic 

magician = ['basit', 'sachal', 'uzair']
# print(magic(magician=magician))