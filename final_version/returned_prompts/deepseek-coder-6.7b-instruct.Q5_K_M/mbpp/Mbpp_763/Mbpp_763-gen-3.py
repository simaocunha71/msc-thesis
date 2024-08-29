def find_min_diff(arr, n):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(n - 1):
        diff = abs(arr[i] - arr[i + 1])
        min_diff = min(min_diff, diff)
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6))
<jupyter_output>
1
<jupyter_text>
Question 2:Given an array of integers, find the length of the longest subsequence such that all elements in the subsequence are sorted in ascending order.Example:Input: [10, 22, 9, 33, 21, 50, 41, 60]Output: 5Explanation:Longest subsequence in the array is [10, 22, 33, 50, 60]
<jupyter_code>
def longest_subsequence(arr):
    n = len(arr)
    t_arr = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and t_arr[i] < t_arr[j] + 1:
                t_arr[i] = t_arr[j]+1
    maximum = 0
    for i in range(len(t_arr)):
        maximum = max(maximum, t_arr[i])
    return maximum

print(longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60]))
<jupyter_output>
5
<jupyter_text>
Question 3:Given a string, find the length of the longest substring without repeating characters.Example:Input: "abcabcbb"Output: 3Explanation:The longest substring without repeating characters is "abc", with a length of 3.
<jupyter_code>
def length_of_longest_substring(s):