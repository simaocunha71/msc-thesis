def sum_list(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

print(sum_list([10,20,30],[15,25,35]))
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
<jupyter_output>
[25, 45, 65]
<jupyter_text>
Problem 3Write a function that takes as input a list of integers and returns the product of the integers.
<jupyter_code>
