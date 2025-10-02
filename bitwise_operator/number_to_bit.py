def convert_number_binary(number):
    if number == 0:
        return "0"
    res = ""
    while number > 0:
        rem = number % 2
        number //= 2
        res = str(rem) + res
    return res

number = 2
res = convert_number_binary(number)
print(res)
