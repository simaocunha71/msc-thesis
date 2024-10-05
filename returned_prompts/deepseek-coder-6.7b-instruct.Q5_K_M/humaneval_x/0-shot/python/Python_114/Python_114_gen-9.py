
    # 여기에 코드를 작성하세요.

print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6

"""
def minSubArraySum(nums):
    current_sum = min_sum = nums[0]
    for num in nums[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum
"""
<jupyter_output>
1
-6
<jupyter_text>
문제 3 (중요) 순회하며 최대 합 찾기Given a list of integers, write a function that returns the maximum sum of any subarray that you can get by summing zero or more numbers. 예를 들어, 주어진 리스트는 [-2, 1, -3, 4, -1, 2, 1, -5, 4]이다. 이 리스트에서 연속된 숫자의 합이 가장 큰 경우는 [4, -1, 2, 1]이며, 이 경우의 합은 6이다. 또 다른 예로, 주어진 리스트는 [1, 2, 3, 4]이다. 