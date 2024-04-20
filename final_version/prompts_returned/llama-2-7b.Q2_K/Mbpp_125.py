"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
class Solution:
    def lengthOfMaximumSubstring(self, s):
        """
        :param s: "110000000011"
        :return: 5
        """
        n = len(s) + 1
        res = []
        
        for i in range(2**n-1,-2**n+1):
            if s[i] == '1':
                curr_val = n - i
            else:
                curr_val = i
            
            dp = [0]*(len(res)+1)
            dp[0] = 1
            
            for j in range(1, len(dp)):
                if s[curr_val+j-1] == '1':
                    curr_val += 2**j - 1
                    
                dp[j]=max(dp[j], dp[j-1]) + (s[curr_val+j-1] - '0') * 2**(len(res)-j)
            
            res = [x for x in res if x < curr_val < res[-1]]        
        return max(res)+2
                     