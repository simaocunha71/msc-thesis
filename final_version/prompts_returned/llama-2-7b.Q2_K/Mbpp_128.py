"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
class Solution:
    def longWords(self,n:int,s: str) -> List[str]:
        ans = []
        for j in range(0, n-1):
            if (j+1)%2==1 and s[-j] == 'e' or s[:len(s)-(i-1)] is not None:
                continue
            else:
                ans.append(s[i])
        return ans