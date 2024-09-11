def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)  # using generator expression and sum function
    # return sum([sum(int(digit) for digit in str(num)) for num in lst])  # using list comprehension and sum function
    # return sum(map(sum, (sum(int(digit) for digit in str(num)) for num in lst)))  # using map and sum function
    # return sum(map(sum, map(lambda x: list(map(int, str(x))), lst)))  # using map and lambda function
    # return sum(map(lambda x: sum(map(int, str(x))), lst))  # using map and lambda function
    # return sum(sum(map(int, str(num))) for num in lst)  # using generator expression and sum function
    # return sum(map(lambda x: sum(int(digit) for digit in str(x)), lst))  # using map and lambda function
    # return sum(sum(map(int, str(x))) for x in lst)  # using generator expression and sum function
    # return sum(map(sum(map(int, str(x))), lst))  # using map and sum function
    # return sum(sum(map(int, str(x))) for x in lst)  # using generator expression and sum function
    # return sum(map(lambda x: sum(map(int, str(x))), lst))  # using map and lambda function
    # return sum(map(sum(map(int, str(x))), lst))  # using map and sum function
    # return sum(map(lambda x: sum(int(digit) for digit in str(x)), lst))  # using map and lambda function
    # return sum(map(sum(map(int, str(x))), lst))  # using map and sum function
    # return sum(map(lambda x: sum(int(digit) for digit in str(x)), lst))  # using map and lambda function
    # return sum(map(sum(map(int, str(x))), lst))  # using map and sum function
    # return sum(map(lambda x: sum(map(int, str(x))), lst))  # using map and lambda function
    # return sum(map(sum(map(int, str(x))), lst))  # using map and sum function
    # return sum(map(lambda x: sum(int(digit) for digit in str(x)), lst))  # using map and lambda function
    # return sum(map(sum(map(int, str(x))),