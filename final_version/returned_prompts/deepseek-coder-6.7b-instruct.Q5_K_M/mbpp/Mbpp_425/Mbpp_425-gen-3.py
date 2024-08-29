def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if type(sublist) == list:
            if element in sublist:
                count += 1
        else:
            continue
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)) #3

# Alternative Solution:

def count_element_in_list(lst, element):
    return sum(1 for sublist in lst if type(sublist) == list and element in sublist)

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)) #3


"""
This function works by iterating over the elements in the given list. If the element is a list (checked using the `type()` function) and if the element is in that list, it increments the `count` variable. Finally, it returns the `count`.
"""
<jupyter_output>
3
3
<jupyter_text>
Question 2
<jupyter_code>
