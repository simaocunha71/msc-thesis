def count_element_in_list(lst, x):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(x)
        else:
            if sublist == x:
                count += 1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))

"""
This function uses a loop to iterate through the elements in the list. If the element is a list, it counts the number of occurrences of the target element in the sublist. If the element is not a list, it checks if the element is equal to the target and if so, increments the count by one. Finally, it returns the count.
"""
<jupyter_output>
3
<jupyter_text>
