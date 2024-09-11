def lps(s):
    # Initialize DP table
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # Initialize base case
    for i in range(n):
        dp[i][i] = 1
    # Fill DP table
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

def test_lps():
    assert lps("TENS FOR TENS") == 5
    assert lps("ABCDABCD") == 4
    assert lps("ABCD") == 1

if __name__ == "__main__":
    test_lps()
    print("All tests passed")






"""
Explanation:
We use dynamic programming to solve this problem. We can think of the longest palindromic subsequence as the maximum sum of a subarray of the DP table.
The DP table will have a size of n by n, where n is the length of the given string. Each cell dp[i][j] in the table represents the length of the longest palindromic subsequence of the substring s[i:j+1].
We initialize the DP table by setting the diagonal cells to 1, as any single character is a palindrome.
Then, we start filling in the DP table from the second-to-last row to the first row, and from the second-to-last column to the first column.
For each cell dp[i][j], if the characters at indices i and j in the given string are the same, we set the length of the palindromic subsequence to be the length of the palindromic subsequence of the substring without the first and last characters plus 2. Otherwise, we take the maximum length of the palindromic subsequences of the substrings