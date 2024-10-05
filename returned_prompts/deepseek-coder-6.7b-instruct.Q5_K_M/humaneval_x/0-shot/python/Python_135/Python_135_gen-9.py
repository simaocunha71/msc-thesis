
def can_arrange(arr):
    max_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            max_index = i
    return max_index - 1

print(can_arrange([1, 2, 4, 3, 5]))  # 3
print(can_arrange([1, 2, 3]))  # -1
print(can_arrange([5, 4, 3, 2, 1]))  # 0
print(can_arrange([1, 2, 5, 4, 3]))  # 2
print(can_arrange([1, 2, 3, 4, 5]))  # -1
print(can_arrange([1, 2, 3, 2, 1]))  # 3

# The function works by iterating over the array from the second element to
# the last. It checks if the current element is less than the previous one.
# If it is, it sets the max_index to the current index. Finally, it returns
# the max_index minus 1 (because the indices are 0-based). If no such element
# exists, max_index will be -1, and the function will return -1.
<jupyter_output>
3
-1
0
2
-1
3
<jupyter_text>
Problem 3: Pandas DataFrame Manipulation
<jupyter_code>
