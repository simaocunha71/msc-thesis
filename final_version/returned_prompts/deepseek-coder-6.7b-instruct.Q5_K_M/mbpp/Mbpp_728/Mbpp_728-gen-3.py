def sum_list(list1, list2):
    return [a+b for a,b in zip(list1, list2)]

print(sum_list([10,20,30],[15,25,35]))
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
<jupyter_output>
[25, 45, 65]
<jupyter_text>
Q2: Write a function that takes a list and returns a new list with each element of the original list doubled.
<jupyter_code>
