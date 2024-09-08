def count_same_pair(list1, list2):
    assert len(list1) == len(list2), "Both lists should be of same length"
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # 4

"""
The function works by iterating over the length of the input lists and comparing the values at the same index in each list. If they are equal, it increments a counter. The function then returns this count.
"""
<jupyter_output>
4
<jupyter_text>
Question 2:
<jupyter_code>
