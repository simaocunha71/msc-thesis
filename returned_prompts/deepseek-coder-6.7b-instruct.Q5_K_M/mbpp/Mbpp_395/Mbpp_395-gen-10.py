def first_non_repeating_character(s: str):
    for index, character in enumerate(s):
        if s.count(character) == 1:
            return character
    return None

assert first_non_repeating_character("abcabc") == None
"""
