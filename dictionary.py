# Assosiate a key for a value, retrieve the value with the help of key!
months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Aug": "August",
    "Sept": "September",
}
# print(months["Feb"])
# print(months.get("Jane")) 
print(months.get("Jane", "Not found!"))  # using default, if any value not found

