def is_Sub_Array(main_array, sub_array):
    return sub_array in main_array

print(is_Sub_Array([1,4,3,5],[1,2]))

"""
Explanation:
In this code, we have defined a function is_Sub_Array that checks whether a sub_array is a part of main_array or not. The operator 'in' in python checks whether a list is present in another list or not.
"""

# Output: False

# -------------------------------------- Alternate Solution 

def is_Sub_Array(main_array, sub_array):
    m = len(main_array)
    n = len(sub_array)
    i = 0
    j = 0
    
    while i < m and j < n:
        if main_array[i] == sub_array[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    
    return j == n

print(is_Sub_Array([1,4,3,5],[1,2]))

"""
Explanation:
In this code, we are using two pointers i and j. We start traversing the main_array and sub_array. If the elements in main_array and sub_array are equal, we increment both i and j. If not, we reset j to 0 and increment i by the number of elements traversed in sub_array. We continue this until either j reaches the end of sub_array (i.e., sub_array is found in main_array) or i reaches the end of main_array.
"""

# Output: False
<jupyter_output>
False
False
<jupyter_text>
**Question 2**