def two_unique_nums(lst):
    return list(set(lst))

print(two_unique_nums([1,2,3,2,3,4,5]))

"""
In the above function, we use the 'set' function to remove any duplicates from the list. The 'set' function does not maintain the order of elements, so if you want to keep the original order of elements, you can use a different approach. Here is a version that keeps the original order:
"""

def two_unique_nums(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst

print(two_unique_nums([1,2,3,2,3,4,5]))

"""
In both functions, we iterate over the elements of the list. In the first function, we convert the list to a set and then back to a list. In the second function, we add each element to a new list only if it has not been added before.
"""

assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
