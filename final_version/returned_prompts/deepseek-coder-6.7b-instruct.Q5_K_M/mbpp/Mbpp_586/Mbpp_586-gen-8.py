def split_Arr(arr, n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2))

# OUTPUT: [5, 6, 52, 36, 12, 10]

# Explanation: The function splits the list at the nth element and rearranges the elements so that the first part of the list is moved to the end.
# For example, if n is 2, it will split the list at the third element (5) and then add the first two elements (12 and 10) to the end.
# Hence, the output is [5, 6, 52, 36, 12, 10].

# Please note that in Python, list indices start at 0. So, when n is 2, it means we are splitting at the third element (not the second).
<jupyter_output>
[5, 6, 52, 36, 12, 10]
<jupyter_text>
