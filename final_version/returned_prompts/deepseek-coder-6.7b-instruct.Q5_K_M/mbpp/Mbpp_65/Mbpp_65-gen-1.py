def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total

print(recursive_list_sum([1, 2, [3,4],[5,6]])) # returns 21
"""
The function recursive_list_sum takes a list as a parameter. It then iterates through each element in the list. If the element is a list, it calls itself with the element as the argument, otherwise it adds the element to the total. The function returns the total sum.
"""

"""
The function works by calling itself recursively when it encounters a list. This is known as recursion. Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem. In this case, the function is breaking down a large list into smaller lists until it can add up the individual numbers.
"""
<jupyter_output>
21
<jupyter_text>
