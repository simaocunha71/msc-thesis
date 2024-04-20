"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
from typing import Optional, List

def replace_spaces(string: str):
    """Replace whitespaces with an underscore or vice versa in a given string."""
    
    def _replaceSpaces(s: str) -> str:
        new_str = ''
        
        for c in s:
            if c.isspace():
                new_str += "_"
            else:
                new_str += c
            
        return new_str
    
    return _replaceSpaces(string)

def replace_underscore(s: str):
    """Replace underscores with whitespaces or vice versa in a given string.
    
    assert replace_underscore('Jumanji_The_Jungle') == 'Jumanji The Jungle'
    """
    
    def _replaceUnderscored(s: str) -> str:
        new_str = ''
        
        for c in s:
            if c.isspace():
                new_str += " "_
            else:
                new_str += c
            
        return new_str
    
    return _replaceUnderscored(s)

def replace_spaces_and_underscore(string: str):
    """Replace underscores and whitespaces with an underscore or vice versa in a given string.
    
    assert replace_spaces_and_underscore('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    """ 
    
    def _replaceSpacesAndUnderscores(s: str) -> str:
        new_str = ''
        
        for c in s:
            if c.isspace() or c in ('_'):
                new_str += '_'
            else:
                new_str += c
            
        return new_str
    
    return _replaceSpacesAndUnderscores(s)