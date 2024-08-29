def move_zero(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst

print(move_zero([1,0,2,0,3,4]))

"""
The above function works by iterating through the list and checking if the current element is 0. If it is, the element is removed from the list and appended at the end of the list. This results in all zeros being moved to the end of the list.

However, this solution has a time complexity of O(n^2) because the remove operation on a list in python is O(n) and the for loop runs n times.

A more efficient solution can be achieved by using a single pass through the list:
"""

def move_zero(lst):
    zero_count = lst.count(0)
    lst = [i for i in lst if i != 0]
    lst.extend([0]*zero_count)
    return lst

print(move_zero([1,0,2,0,3,4]))

"""
In this solution, we first count the number of zeroes in the list. Then we create a new list that includes only the non-zero elements of the original list. Finally, we extend the new list with the appropriate number of zeroes. This results in all zeros being moved to the end of the list in a single pass through the list. This solution has a time complexity of O(n).
"""
<jupyter_output>
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
<jupyter_text>
Question 5
<jupyter_code>
