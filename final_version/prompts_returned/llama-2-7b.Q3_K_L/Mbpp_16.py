"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
class Solution:
    def isLowerCaseUnderscore(self, s):
        words = (word for word in s.split() if word == '_')
        all_small = True
        
        for w in words:
            if len(w) > 1 and not w[0].islower():
                return False
            
            elif 'aeiou' in set(w):
                all_small = False
                
        return (all_small)