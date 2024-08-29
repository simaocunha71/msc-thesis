def count_same_pair(list1, list2):
    return sum([1 for i in range(len(list1)) if list1[i] == list2[i]])

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))
<jupyter_output>
4
<jupyter_text>
Q2:
<jupyter_code>
