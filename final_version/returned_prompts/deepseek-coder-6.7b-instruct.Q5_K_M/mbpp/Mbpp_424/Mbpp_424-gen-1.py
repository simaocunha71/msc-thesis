
def extract_rear(tup):
    return [i[-1] for i in tup]

print(extract_rear(('Mers', 'for', 'Vers')))


#Solution 2:

def extract_rear(tup):
    result = []
    for i in tup:
        result.append(i[-1])
    return result

print(extract_rear(('Mers', 'for', 'Vers')))


#Solution 3:

def extract_rear(tup):
    return list(map(lambda x: x[-1], tup))

print(extract_rear(('Mers', 'for', 'Vers')))

"""
In all three solutions, we iterate through each string in the tuple, and append the last character of each string to the result list.
"""

#Solution 4:

def extract_rear(tup):
    return [i[::-1][0] for i in tup]

print(extract_rear(('Mers', 'for', 'Vers')))

"""
In this solution, we reverse each string in the tuple and take the first character, which is the last character of the original string.
"""
<jupyter_output>
['s', 'r', 's']
['s', 'r', 's']
['s', 'r', 's']
['s', 'r', 's']
<jupyter_text>
Question 3:Create a function that takes a list of numbers and returns the sum of all the elements in the list.
<jupyter_code>
#Solution 1:

def sum_elements(lst):
    return sum(lst)

print(sum_elements([1, 2, 3, 4, 5]))


#Solution 2:

def sum_elements(lst):
    return reduce(lambda a, b: a+b, lst)

print(sum_elements([1, 2, 3, 4, 5]))


#Solution 3:

def sum_elements(lst