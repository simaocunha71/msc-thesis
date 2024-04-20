"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
from typing import List, Optional

def start_withp(word: Optional[List[str]] = None) -> Optional[Tuple[str, str]]:
    if not word: return ('', '')

    if len(word) < 2: return (word[0], '')

    for i in range(1, len(word)):
        if word[i] == "p": return (word[:i+1], word[i])

    return ("", "")