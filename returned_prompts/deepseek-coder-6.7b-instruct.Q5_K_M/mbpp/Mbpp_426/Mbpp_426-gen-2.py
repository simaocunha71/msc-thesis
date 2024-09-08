def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 == 0]

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def filter_oddnumbers(lst):
    return list(filter(lambda num: num % 2 == 0, lst))

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def filter_oddnumbers(lst):
    return [num for num in lst if not num % 2]

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OR

def filter_oddnumbers(lst):
    return [num for num in lst if not num % 2]

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
This code will print:
[2, 4, 6, 8, 10]
which are the even numbers from the list.
"""
<jupyter_output>
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
<jupyter_text>
