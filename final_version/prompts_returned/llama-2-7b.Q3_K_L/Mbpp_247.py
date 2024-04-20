"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def findLengthPalindromeSubseqInString(self, s):
        """Write a function to find the length of the longest palindromic subsequence in the given string.
        assert lps("TENS FOR TENS") == 5
        """
        def isPalindrome(s):
            i = len(s)//2
            j = (i - 1) % len(s)
            while i >= j:
                if s[j] == s[i]:
                    return True
                else:
                    return False
            return False
        
        def isPalindromeSubseq(ss):
            n = len(ss)
            
            if n == 0:
                return []
            
            stack = [ss[0]]
            ans = 1
            
            while True:
                i = 0
                j = 0
                
                while (i < n and j < n):
                    if not isPalindromeSubseq(stack[-n:] + ss[j:i]):
                        return ans
                    
                    stack.append(ss[i])
                    
                    if i > 0 and not isPalindrome(stack[-1-i:] + ss[:-j]):
                        while j < n and not isPalindromeSubseq(stack[-n:] + ss[i:j+1]):
                            ans += 1
                    
                    i += 1
                    
                    if i >= n or j >= n:
                        return ans
                stack.append(ss[0])
            
        return len(isPalindromeSubseq(s))
