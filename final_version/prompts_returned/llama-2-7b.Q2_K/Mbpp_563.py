"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(s):
    s = '"%s'" % s  # add quotes around the string that contains values
    idx = -1  # index of a single quote in the string, not part of the result
    result = []
    
    for c in s:
        if c == '"':
            idx +=1
            continue
        
        elif c == "'":
            result.append(s[idx+1:])  # get everything between the last single quote to before next double quote
            idx = -1  # reset the index for next iteration so that it always starts at beginning of string
            break
    if idx >= 0:
        result.append(s[:idx+1])  # add the substring before the quotes
            
    return result