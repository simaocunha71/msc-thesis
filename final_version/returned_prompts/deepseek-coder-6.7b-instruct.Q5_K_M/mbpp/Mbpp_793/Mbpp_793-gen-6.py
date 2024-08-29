
def last(lst, target):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == target:
            return i
    return -1

print(last([1,2,3],1))

# This function iterates from the end of the list to the start. 
# When it finds the target, it returns the index. 
# If it doesn't find the target, it returns -1.
<jupyter_output>
0
<jupyter_text>
Question 3Given the list of list of integers, write a python function to find the sum of the integers in the nested lists.assert nested_sum([[1,2,3], [4,5,6], [7,8,9]]) == 45
<jupyter_code>
