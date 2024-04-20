"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""
from typing import Optional, List

def count_occurances(string):
    # your code here
    str_list = list()
    
    for i, j in enumerate(string):
        if i != j:
            str_list.append((i,j))
    return len([k for k,l in sorted(str_list)])
"""
class Solution:
    def countOccurrences(self, s: str) -> int:
        
        string = ""
        char = 0

        for i in range(len(s)):
            if i != s[i]:
                string += i
                    
                if i == 'std' and char == "":
                    char = "std"
                else:
                    char = ""
        
        return len([k for k,l in sorted(map(tuple,string.split("std")))] )
"""