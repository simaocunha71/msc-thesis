
    def smallest_change(arr):
        changes = 0
        for i in range(len(arr)//2):
            if arr[i] != arr[-i-1]:
                changes += 1
        return changes

    print(smallest_change([1,2,3,5,4,7,9,6]))
    print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
    print(smallest_change([1, 2, 3, 2, 1]))

output:

    4
    1
    0

Explanation:

For the first example, the elements at indices 0, 1, 2 and 5 need to be changed to make the array palindromic.
For the second example, the element at index 4 needs to be changed to make the array palindromic.
For the third example, the array is already palindromic.

"""

def smallest_change(arr):
    changes = 0
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            changes += 1
    return changes

print(smallest_change([1,2,3,5,4,7,9,6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
<jupyter_output>
4
1
0
<jupyter_text>
Problem 16
<jupyter_code>
"""
