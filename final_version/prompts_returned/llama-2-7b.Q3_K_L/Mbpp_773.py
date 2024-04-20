"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""

class Solution(object):
    def occurrences(self, s: str, p: str) -> List[int]:
        """
        Do not return anything if there is no match.
        1. find the positions of first letter in each substrings
        2. find the positions of second letter in each substrings
        3. check if these two positions matches and return True
            1. find the occurrence of substring within a string
        """
        occurances = [0 for _ in range(len(p))] #initialize array with all 1's, which means no occurance
        sub_positions = [[],[],[]]
        first_letter = False
        for i in range(len(p)):
            if p[i] == s[0]:
                first_letter = True
            else:
                first_letter = False
            last_first_letter = first_letter
            sub_positions[0].append((i,last_first_letter))  # first position of substring is in the beginning
            
        for j in range(len(p)):
            if p[j] == s[-1]:
                last_sub_position = i
                first_letter = False
            else:
                last_sub_position = len(s) - 1 # last position of substring is on the end
                first_letter = True
            
        for i in range(len(p)):
            if sub_positions[0][i] == [last_first_letter, last_sub_position] and sub_positions[2][i] == [first_letter , last_sub_position]:
                occurances[i]=True
        return occurances
