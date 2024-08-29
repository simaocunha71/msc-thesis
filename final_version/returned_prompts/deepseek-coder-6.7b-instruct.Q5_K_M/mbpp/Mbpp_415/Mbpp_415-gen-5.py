def max_Product(nums):
    max_product = 0
    num1 = num2 = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]*nums[j] > max_product:
                max_product = nums[i]*nums[j]
                num1 = nums[i]
                num2 = nums[j]
    return (num1, num2)

print(max_Product([1,2,3,4,7,0,8,4]))

# Another approach is sorting the array and then returning the last two elements.
def max_Product_sorted(nums):
    nums.sort()
    return (nums[-1], nums[-2])

print(max_Product_sorted([1,2,3,4,7,0,8,4]))
<jupyter_output>
(7, 8)
(7, 8)
<jupyter_text>
Q2:Given an array of integers, find the length of the longest increasing subsequence.Example:```Input: [10,9,2,5,3,7,101,18]Output: 4 Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.```
<jupyter_code>
def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))
<jupyter_output>
4
<jupyter_text>
Q3: Given an array of integers, find