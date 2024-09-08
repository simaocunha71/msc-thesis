def count_same_pair(list1, list2):
    assert len(list1) == len(list2)
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # 4
"""
Explanation: 
In the given lists, the values at index 0, 3 and 5 are the same. So, the function should return 3.
"""
<jupyter_output>
4
<jupyter_text>
Exercise 2
<jupyter_code>
