def max_Product(arr):
    arr.sort()
    n = len(arr)
    # two highest numbers
    if (arr[0] * arr[1]) > (arr[n - 1] * arr[n - 2]):
        return (arr[0], arr[1])
    else:
        return (arr[n - 1], arr[n - 2])

print(max_Product([1,2,3,4,7,0,8,4])) # returns (7, 8)

"""
Explanation:
The idea is to sort the given array. After sorting, we have two cases:
1) If product of first two numbers is greater than product of last two numbers, we get the pair (arr[0], arr[1]).
2) Else we get the pair (arr[n-1], arr[n-2]).
"""

# Time complexity is O(n log n) due to sorting.
# Space complexity is O(1) as no extra space is used.

# Note: This solution assumes that there are at least two positive numbers in the array.
# If there is a possibility of negative numbers, then the pair with highest product can be obtained by comparing two smallest negative numbers with two largest positive numbers.
# However, this solution would not work in that case, we would need to find the two smallest negative numbers and the two largest negative numbers.
# We can add a condition to check if there are at least two negative numbers in the array.
# If yes, then we can return the pair with the highest product if we multiply the two smallest negative numbers with the two largest positive numbers.
# If no, then we return the pair with the highest product as explained above.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:
<jupyter_code>
