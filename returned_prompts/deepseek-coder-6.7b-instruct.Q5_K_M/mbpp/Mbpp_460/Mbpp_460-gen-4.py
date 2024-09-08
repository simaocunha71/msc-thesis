
def Extract(lst):
    return [i[0] for i in lst if isinstance(i, list)]

print(Extract([[1, 2, 3], [4, 5], [6], []]))

#output: [1, 4, 6]
<jupyter_output>
[1, 3, 6]
[1, 4, 8]
[1, 4, 6]
<jupyter_text>
Question 2:Write a python function that takes a list of integers and returns a new list with the squares of the elements in the original list.
<jupyter_code>
def square_elements(lst):
    return [i**2 for i in lst]

print(square_elements([1, 2, 3,