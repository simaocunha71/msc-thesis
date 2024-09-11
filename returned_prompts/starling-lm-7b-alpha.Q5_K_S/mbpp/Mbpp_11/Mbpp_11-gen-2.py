"""
def remove_Occ(s,c):
    i = 0
    while i < len(s) and s[i] != c:
        i += 1
    j = len(s) - 1
    while j >= 0 and s[j] != c:
        j -= 1
    return s[i+1:j]
"""

