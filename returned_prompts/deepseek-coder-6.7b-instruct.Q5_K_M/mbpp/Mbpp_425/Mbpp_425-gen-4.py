def count_element_in_list(lst,ele):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(ele)
        else:
            if sublist == ele:
                count += 1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1))

#Output: 3

"""
Here is a breakdown of how the program works:

The function count_element_in_list takes in two parameters: a list (lst) and an element (ele). It initializes a count variable to 0.

The function then iterates over each element in the list. If the element is a list, it increments the count by the number of times the element appears in that list.

If the element is not a list, it checks if it is equal to the element. If it is, it increments the count.

Finally, it returns the count.
"""
<jupyter_output>
3
<jupyter_text>
Question 3
<jupyter_code>
