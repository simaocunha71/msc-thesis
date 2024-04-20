"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""

def occurance_substring(s: str, substring:str):
    count = 0
    match = False
    result = None
    
    for ch in s:
        if ch == substring:
            count +=1
            match = True
        
    return (match, count ,-1)
print(occurance_substring('python programming, python language','python'))