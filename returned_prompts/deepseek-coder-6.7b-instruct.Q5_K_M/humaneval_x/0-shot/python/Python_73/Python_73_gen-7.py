
    def smallest_change(arr):
        n = len(arr)
        if n <= 1:
            return 0

        left, right = 0, n - 1
        change = 0

        while left < right:
            if arr[left] != arr[right]:
                change += 1
            left += 1
            right -= 1

        return change

print(smallest_change([1,2,3,5,4,7,9,6])) # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
print(smallest_change([1, 2, 3, 2, 1])) # 0

# Time complexity of this solution is O(n), where n is the length of the array.
# This is because we only iterate through the array once, comparing each pair of elements.
# The space complexity is O(1), as we only use a constant amount of space to store the indices and the change count.

# This solution works by using a two-pointer technique. The left pointer starts at the beginning of the array, and the right pointer starts at the end.
# We then increment the left pointer and decrement the right pointer, comparing the elements at these positions.
# If the elements are not equal, we increment the change count. We repeat this process until the left pointer is less than the right pointer.
# At the end, we return the change count, which represents the minimum number of changes needed to make the array palindromic.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 1
<jupyter_code>
def sum_of_digits(n):
    """
    Given a non-negative integer n, return the sum of its digits.

    For example:
    sum_of_digits(1234) == 10
    sum_of_digits(5678) == 26
    """
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(1234)) # 10
print