
def recursive_list_sum(lst):
    total = 0
    for element in lst:
        if type(element) == list:
            total += recursive_list_sum(element)
        else:
            total += element
    return total

print(recursive_list_sum([1, 2, [3,4],[5,6]]))  # Output: 21


"""
Explanation:
The function recursive_list_sum takes a list as an argument. It initializes a variable total to 0. Then it loops over the elements of the list.
If an element is a list, it calls itself (the function recursively) on that element and adds the result to total.
If an element is not a list, it simply adds the element to total.
Finally, it returns the total sum.
"""

# Test cases
print(recursive_list_sum([1, 2, [3, 4, [5, 6, [7, 8]]], 9]))  # Output: 36
print(recursive_list_sum([1, 2, [3, 4], 5, 6, [7, 8, 9]]))  # Output: 45
print(recursive_list_sum([1, 2, [3, 4], 5, 6, [7, 8, 9]]))  # Output: 45
print(recursive_list_sum([1, 2, [3,4],[5,6]]))  # Output: 21
print(recursive_list_sum([1, 2, [3,4,5,6]]))  # Output: 21
print(recursive_list_sum([1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]))  # Output: 45
<jupyter_output>
21
36
45
21
21
45
<jupyter_text>
