def first_non_repeating_character(s: str) -> str:
    frequency = {}
    for c in s:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    
    for c in s:
        if frequency[c] == 1:
            return c
    
    return None