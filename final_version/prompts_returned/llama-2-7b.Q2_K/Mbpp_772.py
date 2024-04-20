"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
from typing import Optional, List

def remove_length(strng: str) -> str:
    """
    :type strng: str
    """
    length = len(strng)-1
    words = list()
    
    for i in range(len(strng)):
        if strng[i].isalpha():
            words.append(str(strng[:i])+' '+str(strng[i:]))
            
        
        
    length = max([len(word) for word in words]) 
    
    return ''.join([' '.join(map(str, part)) for part in words if part and len(part)<length])
