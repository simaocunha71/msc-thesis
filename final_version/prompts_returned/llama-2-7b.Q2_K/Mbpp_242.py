"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
class Solution:
    def countCharacters(self, s):
        c = 0;
        
        for i in range(0, len(s), 3):
            if s[i] not in "aeiou":
                continue
            else:
                c += 1
                
        return c