def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))

"""
The function above takes two lists as input. It then loops through each index of the lists and checks if the values at that index are equal. If they are, it increments a counter. After all indices have been checked, it returns the counter.
"""
<jupyter_output>
4
<jupyter_text>
Question 2:
<jupyter_code>
