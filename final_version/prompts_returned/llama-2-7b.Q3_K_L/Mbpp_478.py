"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
from typing import List, Optional

class Solution:
    def removeDuplicates(self, A: str) -> str:
        if not A or len(A) == 1 or len(set(A)) == len(A):
            return A
        
        return "".join([x for x in A if x.isupper()])

def main():
    test_str = "PYTHon"
    print(Solution().removeDuplicates(test_str))
    
if __name__ == '__main__':
    main()
