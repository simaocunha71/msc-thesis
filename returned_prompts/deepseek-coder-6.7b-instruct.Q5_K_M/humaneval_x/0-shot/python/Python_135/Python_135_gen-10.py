
def can_arrange(arr):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            return i
    return -1

print(can_arrange([1,2,4,3,5]))  # 3
print(can_arrange([1,2,3]))  # -1


# Explanation:
# In the first example, the largest index of an element which is not greater than or equal to the element immediately preceding it is 3.
# In the second example, all the elements are in increasing order, so no such element exists.

# Complexity Analysis:
# The time complexity of the code is O(n), where n is the length of the array. This is because it needs to iterate through the array once to find the required index.
# The space complexity is O(1), as no additional space is used.
<jupyter_output>
<empty_output>
<jupyter_text>
11. Write a Python function to get the nth Fibonacci number.
<jupyter_code>
# 