def occurance_substring(s, sub):
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            return (sub, i, i+len(sub))
    return None

# assert occurance_substring('python programming, python language','python')==('python', 0, 6)

"""
Write a function that takes a string and two substrings as arguments and returns True if both substrings appear in the string, and False if either or neither substring does not appear in the string. If the substrings overlap, it should be considered as an invalid input.
assert check_substring('python programming, python language', 'python', 'language') == True
"""

def check_substring(s, sub1, sub2):
    if len(sub1) > len(sub2):
        sub1, sub2 = sub2, sub1
    if s.count(sub1) == 0 or s.count(sub2) == 0:
        return False
    elif s.find(sub1) >= s.find(sub2) and s.find(sub2) != -1:
        return True
    else:
        return False

# assert check_substring('python programming, python language', 'python', 'language') == True

"""
Write a function that takes a string and a dictionary of substrings and their meanings as arguments and returns a dictionary of the positions of the substrings within the string. Return None if there is no match.
assert get_positions('python programming, python language', {'python': 'a programming language'}) == {'python': [0, 6]}
"""

def get_positions(s, subs):
    ret = {}
    for k, v in subs.items():
        for i in range(len(s)):
            if s[i:i+len(k)] == k:
                ret[k] = [i]
                break
        else:
            ret[k] = None
            break
    return ret

# assert get_positions('python programming, python language', {'python': 'a programming language'}) == {'python': [0, 6]}

"""
Write a function that takes a string