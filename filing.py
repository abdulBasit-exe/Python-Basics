# file= open("basic.txt", "r+")
# print(file.readline())
# file.close()
# for i in file:
#     print(i)

file = open("index.html", "w")
file.write("<p>This is a html page<p>")
file.close()

def random_fun(random):
    return random

print(random_fun(random="1"))
# file= open("basic.txt", "r")
# print(file.read())