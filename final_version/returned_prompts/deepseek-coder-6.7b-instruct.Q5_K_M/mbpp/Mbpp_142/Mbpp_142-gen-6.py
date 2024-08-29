"""
Here is a solution for the problem:
"""

def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])) # should return 3

"""
This solution works by iterating through each item in the first list, and comparing that item to the corresponding item in the second and third lists. If all three lists have the same item in the same position, the counter is increased. At the end of the loop, the function returns the count of identical items.
"""
<jupyter_output>
3
<jupyter_text>
Question 2:
<jupyter_code>
