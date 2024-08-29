
def neg_nos(lst):
    return [i for i in lst if i < 0]

print(neg_nos([-1,4,5,-6]))

#output: [-1, -6]

# This program uses a list comprehension to filter out the negative numbers from the given list. The condition i < 0 checks if a number is less than 0 (i.e., negative). If it is, it gets added to the new list.
<jupyter_output>
[-1, -6]
<jupyter_text>
6. Write a python function that takes a list of numbers as an argument and returns a dictionary where the keys are the indices and the values are the squares of the elements at those indices.For example, assert square_dict([1,2,3,4,5]) == {0: 1, 1: 4, 2: 9, 3: 16, 4: 25}
<jupyter_code>
# 