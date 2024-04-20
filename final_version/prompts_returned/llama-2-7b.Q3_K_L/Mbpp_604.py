"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
from typing import List, Optional

class Solution:
    def reverseWords(self, word:str) -> str:
        """
        Do not return anything if the input is empty. 
        Otherwise, return a space-separated list of its words in reverse order.
        Example:
        Given s = "Hello, LeetCode", return ["LeetCode , Hello"].
        """
        stack=[]
        for i in range(len(word)):
            if word[i] == ',':
                while len(stack) and stack[-1][0] !=word[i]:
                    stack.pop()
                stack.append((word[i],word))
            else:
                stack.append([word[i],word])
        reversed_words = ""
        for i in range(len(stack)):
            if len(reversed_words) != 0 and reversed_words[-1][-1] == '.':
                    reversed_words += " "
                reversed_words += stack[i][0]+' '  
        return reversed_words[:-1]
