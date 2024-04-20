"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
from typing import Any, List, Optional, Set, Tuple, Type, Union, Dict
import collections

class Trie:
    def __init__(self) -> None:
        self.__root__ = Trie()
    
    def add_word(self, word: str) -> None:
        self.__root__.add_child(word[0])
        
        for c in word[1:]:
            if self.__root__.children.get(c):
                self.__root__ = self.__root__.children[c]
            else:
                self.__root__.add_child(c)
                
    def add_word_backward(self, word: str) -> None:
        if not self.__root__.add_word(word):
            return False
        for c in word[:-1]:
            if self.__root__.children.get(c):
                self.__root__ = self.__root__.children[c]
            else:
                self.__root__.add_child(c)
                
    def __contains__(self, subword : str) -> bool:
        for c in subword:
            if not self.find_backward(subword[:-1], c):
                return False
        return True
    
    def find_backward(self, word: str, chr: str )-> bool:
        self.__root__.children[chr].find_backward(word + chr)
        
    
    def __iter__(self) -> "TrieIterator":
        itr = TrieIterator(self.__root__.children)
        return iter(itr)
        
def max_run_uppercase(text: str) -> int:
    text += '*' * 100
    
    def _find_max_run_uppercase(text:str, i:int) -> Optional[Any]:
        word = text[i]
        
        if (word.isalpha() and word in set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
            return max([_find_max_run_uppercase(text, i + 1)] or [0])
        else:
            return _find_max_run_uppercase(