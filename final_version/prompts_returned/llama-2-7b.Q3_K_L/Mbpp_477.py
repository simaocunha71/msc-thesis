"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
from typing import Any, List, Optional

class Solution:
    def __init__(self, dictionary: Optional[List[str]]):
        self.__dictory = [None] * (len(dictionary) + 1)
        self.dict = list(dictionary)
    
    def lowercase(self, s: str) -> str:
        length = len(s)
        for i in range(length - 1):
            if not self.__dictory[i] or self.__dictory[i][0] != s[i]:
                if s[i].islower():
                    self.dict.append(self.__dictory[i + 1])
                    self.__dictory[i] = (s[i], self.dict[-1])
        return self.__dictory[length - 1][0]
    
def main(args):
    dictionary = [["abc", "xyz"], ["abc", "xyzy"]]
    print("""
    Write a python function to convert the given string to lower case.
    """ + "\n" * (len(dictionary) - 2))
    func: Any[str, List[Any]] = None
    if dictionary:
        func = "lowercase"
    
if __name__ == '__main__':
    main(sys.argv[1])