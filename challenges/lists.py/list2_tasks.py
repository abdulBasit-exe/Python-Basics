places = ["mithi", "swat", "thar", "thatta","ladakh"]

print(places)
print(sorted(places))
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)

places.sort(reverse=True)
print(places)

for names in places:
    print(names.title())
