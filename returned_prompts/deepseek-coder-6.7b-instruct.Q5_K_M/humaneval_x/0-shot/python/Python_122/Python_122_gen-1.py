
def add_elements(arr, k):
    return sum(x for x in arr[:k] if len(str(abs(x))) <= 2)

print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # 24
print(add_elements([-123,456,789], 2)) # -123
print(add_elements([5000, 5000, 5000], 3)) # 15000

# Time complexity: O(n)
# Space complexity: O(n)
<jupyter_output>
24
-123
15000
<jupyter_text>
Problem 13:Given a non-empty array of integers, return the third maximum number in the array. If it does not exist, return the maximum number instead.Example:Input: [3, 2, 1, 5, 6]Output: 3Explanation: The third maximum number is 3.Constraints:1 <= len(arr) <= 10^4-10^9 <= arr[i] <= 10^9
<jupyter_code>
