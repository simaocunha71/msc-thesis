"""
Write a python function to find the index of smallest triangular number with n digits. 
assert find_Index(2) == 4
"""
from typing import List, Optional

def find_Index(n:int):
    """Find the index."""
    ans = ""
    
    for i in range(n+1):
        if (i-1)*(i-1) <= n**2:
            if int(str(n**0.5)) < len(ans):
                ans += str(int(str(n))) 
        
    return int(find_Index(len(ans)))