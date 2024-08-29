def square_nums(num_list):
    return [num**2 for num in num_list]

print(square_numnums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def square_nums(num_list):
    return list(map(lambda num: num**2, num_list))

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def square_nums(num_list):
    return [num*num for num in num_list]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def square_nums(num_list):
    return [pow(num, 2) for num in num_list]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def square_nums(num_list):
    return list(map(pow, num_list, [2]*len(num_list)))

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def square_nums(num_list):
    return [num*num for num in num_list]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
