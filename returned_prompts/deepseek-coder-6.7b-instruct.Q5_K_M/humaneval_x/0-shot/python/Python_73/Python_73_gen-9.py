
    def smallest_change(arr):
        n = len(arr)
        changes = 0

        # Compare elements from start and end of list
        for i in range(n // 2):
            if arr[i] != arr[n - i - 1]:
                changes += 1

        return changes


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))  # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # 1
print(smallest_change([1, 2, 3, 2, 1]))  # 0

"""
The solution works by iterating over the first half of the array and comparing each element with the corresponding element
at the end of the array (from the start). If they are not equal, we increment our `changes` counter by 1.

Finally, we return the total number of changes, which is the minimum number of elements that need to be changed to make the
array palindromic.
"""

"""
Time complexity: O(n), where n is the length of the array, as we're only iterating over the array once.
Space complexity: O(1), as we're only using a constant amount of extra space to store the `changes` counter and the length of the array.
"""

"""
The solution works by iterating over the first half of the array and comparing each element with the corresponding element
at the end of the array (from the start). If they are not equal, we increment our `changes` counter by 1.

Finally, we return the total number of changes, which is the minimum number of elements that need to be changed to make the
array palindromic.
"""

"""
Time complexity: O(n), where n is the length of the array, as we're only iterating over the array once.
Space complexity: O(1), as we're only using a constant amount of extra space to store the `changes` counter and the length of the array.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 