# multiple values in a single item
universities= ["Muet", "NED", "IBA", "Sindh Uni"]
# print(universities[1:3]) # ned, iba
# print(universities[-1]) # Sindh Uni
other_Unis = ["Isra_Uni", "K_IBA", "Sir_Syed"]
universities.extend(other_Unis) # merging two lists
# print(universities)
# universities.insert(1, "Aror_Uni") # updating the lists
# print(universities)
# universities.remove("Muet") # removing any element
# print(universities)
# universities.pop() # pop- removes last element
# print(universities.index("K_IBA")) 
universities.sort()
# print(universities)
uni2 = universities.copy()
print(uni2)



