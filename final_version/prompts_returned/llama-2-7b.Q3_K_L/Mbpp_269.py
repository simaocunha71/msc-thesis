"""
Write a function to find the ascii value of a character.
assert ascii_value('A')==65
"""
class Solution(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
    def dictValue(self, char):
        return self.dictionary[char]

solution = Solution({'!':31,'@':'40','#':'45','$':'48','%':'62','^':'57',
                  '&':'38','*':'42','+':'49','|':'61','-':'45','/':'47','\\':'58'})
print solution.dictValue('A')