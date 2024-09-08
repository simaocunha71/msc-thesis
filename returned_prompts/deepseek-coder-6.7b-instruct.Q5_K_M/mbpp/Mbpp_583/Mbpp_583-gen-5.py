def catalan_number(n):
    if n<=1:
        return 1
    catalan = [0 for _ in range(n+1)]
    catalan[0] = 1
    catalan[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j]*catalan[i-j-1]
    return catalan[n]

print(catalan_number(10))

# Time complexity: O(n^2)
# Space complexity: O(n)

assert catalan_number(10)==16796

# This code is contributed by "Sharad Sidhanti".
<jupyter_output>
16796
<jupyter_text>
**Question 4**Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.Examples:Input: arr[] = {1, 9, 3, 10, 4, 20, 2}Output: 4Explanation: The subsequence {1, 2, 3, 4} is the longest subsequenceof consecutive elementsExample 2:Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 45}Output: 5Explanation: The subsequence {36, 35, 34, 33, 34} is the longestsubsequence of consecutive elements.**Solution:**
<jupyter_code>
def findLongestConseqSubseq(arr):
    s = set() 
    ans = 0
    for ele in arr:
        s.add(ele)
    for i in range(len(arr)):
        if (arr[i]-1) not in s:
            j = arr[i]
            while(j in s):
                j += 1
            ans = max(ans, j - arr[i])
    return ans 

