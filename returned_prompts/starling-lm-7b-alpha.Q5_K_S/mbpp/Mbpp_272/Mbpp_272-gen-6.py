def rear_extract(input_list):
    rear_list = []
    for i in input_list:
        rear_list.append(i[2])
    return rear_list

# Here is the solution:
def rear_extract(input_list):
    return [i[2] for i in input_list]

# Testing the function
input_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
assert rear_extract(input_list) == [21, 20, 19]

# Here's an alternative method using list comprehension:
def rear_extract(input_list):
    return [i[2] for i in input_list]

# Testing the function
input_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
assert rear_extract(input_list) == [21, 20, 19]

# Here's a simpler version using map() and lambda function:
def rear_extract(input_list):
    return list(map(lambda i: i[2], input_list))

# Testing the function
input_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
assert rear_extract(input_list) == [21, 20, 19]

# Here's a method using filter() and lambda function:
def rear_extract(input_list):
    return list(filter(lambda i: i[2] != None, input_list))

# Testing the function
input_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
assert rear_extract(input_list) == [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# Here's a method using