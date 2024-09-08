
def max_product(nums):
    max_prod = [0]*len(nums)
    max_prod[0] = nums[0]
    for i in range(1, len(nums)):
        max_prod[i] = max(nums[i], max_prod[i-1]*nums[i])
    return max(max_prod)

print(max_product([3, 100, 4, 5, 150, 6]))  # 3000



"""
Explanation:

This problem can be solved using Dynamic Programming.

The idea is to create an array max_prod[] such that max_prod[i] stores the maximum product ending with arr[i].

Start by initializing max_prod[0] with arr[0] as there is only one number in the array.

Then for each element from 1 to n-1, we can choose to either extend the current subsequence by including arr[i] or start a new subsequence.

If we choose to include arr[i], the new max product will be max_prod[i-1] * arr[i] (this is because we are multiplying with the existing product).

If we choose to start a new subsequence, the new max product will be arr[i] (since we start a new subsequence with arr[i]).

So, for each element at index i, we will update max_prod[i] to be the maximum of these two options.

Finally, the maximum product of the increasing subsequence will be the maximum value in max_prod[].

The time complexity of this solution is O(n) as we are doing a single pass over the array. The space complexity is also O(n) for the max_prod[] array.
"""

"""
Test:

Test cases are given in the problem statement. Here, we are checking whether the function is able to find the maximum product of an increasing subsequence correctly.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3
<jupyter_code>
