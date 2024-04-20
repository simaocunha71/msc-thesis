"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        :type s: str
        :rtype: List[int]
        """
        from collections import Counter
        my_dict = Counter(s) # Counter is a dictionary of strings to integers.
        my_list = [] # Initialize the empty list
        
        for string in sorted(my_dict, key=len): # Sort by length and then alphabetically (using c-str, which sorts alphabeticly).
            start_index = s.find(string) + len(s) - 1 # Get the last index of substring's first character.
            my_list.append((start_index, string)) # Append the substring and its length to the list.
        
        return sorted(my_list) # Convert the list into a new list with same elements in sorted order.
