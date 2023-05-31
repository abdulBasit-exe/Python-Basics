# print(3**2)

# using a for loop to do this. An Exponent Function.function

def raise_to_power(base_num, pow_num):
    result =1
    for i in range(pow_num):
        result = result* base_num
    return "Result: "+str(result)

print(raise_to_power(8,2))
