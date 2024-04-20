"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""
from typing import Optional

def word_len(word: str) -> bool:
  if len(word) % 2 != 0:
    return True
  else:
    return False