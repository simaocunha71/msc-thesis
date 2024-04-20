"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
class Solution(object):
    def __init__(self):
        self.map = {
            str: {int: False},
            int : {str: False},
            bool : {str: False}
        }
    def checkType(self, t):
        """
        :type t: List[Any]
        :rtype: bool
        """
        for item in t:
            if not self.checkType(item) or type(item) is str:  # if any one element of tuple is string we cannot compare with other elements.
                return False
        for key, val in self.map.items():
            if (val[type(t[0])] == True and key not in t):
                return False
        return True
