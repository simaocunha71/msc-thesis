"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""
class Solution:
    def __init__(self):
        self.res = []
        
#     def split(self, s): # 1405
#         if not len(s) > 0: return [ ]
#         for c in s:
#             if not ord(c) <= 256 or ord(c) >= 128:
#                 self.res.append(ord(c))
    
    def split(self, s): # 1407
        if not len(s) > 0: return [ ]
        for c in s:
            self.res.append(ord(c))
            
        