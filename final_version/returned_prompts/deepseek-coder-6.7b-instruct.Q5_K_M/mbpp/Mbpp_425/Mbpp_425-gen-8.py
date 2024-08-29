def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if type(sublist) is list:
            count += sublist.count(element)
        else:
            if sublist == element:
                count += 1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)) # Output: 3

"""
This function traverses through each element in the main list.
If the element is a list, it checks how many times the element occurs in the sublist.
If the element is not a list and matches the target element, it increments the count.
"""

# Time complexity: O(n*m), where n is the number of elements in the main list and m is the average number of elements in the sublists
# Space complexity: O(1), constant space as no additional space is used.
<jupyter_output>
3
<jupyter_text>
Question 3
<jupyter_code>
