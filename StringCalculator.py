import numbers


def add(string):
    # addition for more then 1 number using sum()
    string_numbers = string.split(",")
    numbers =[]
    for i in string_numbers:
        try:
            number = int(i)
        except ValueError:
            number =0
        numbers.append(number)
    #check string empty or 1 number
    return sum(numbers)
    if string == "1":
        return 1
    else:
        return 0
    