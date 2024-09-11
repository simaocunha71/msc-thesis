def string_to_list(string):
    return string.split(" ")

def test_string_to_list():
    assert string_to_list("python programming")==['python','programming']

test_string_to_list()




"""
Given a string, find all the substrings of the string. 
The string is assumed to be lowercase and not contain any special characters.
"""

def all_substrings(string):
    if len(string)==0:
        return []
    if len(string)==1:
        return [string]
    else:
        prev_list=all_substrings(string[1:])
        curr_list=[]
        for s in prev_list:
            curr_list.append(s)
            curr_list.append(s+string[0])
        return curr_list

def test_all_substrings():
    assert all_substrings("python")==['py','yt','th','ho','on','po','ph','hn']

test_all_substrings()


"""
Given a string, find all the substrings of the string that contain only the letters a, c, or t.
The string is assumed to be lowercase and not contain any special characters.
"""

def valid_substrings(string):
    if len(string)==0:
        return []
    if len(string)==1:
        if string in ['a','c','t']:
            return [string]
        else:
            return []
    else:
        prev_list=valid_substrings(string[1:])
        curr_list=[]
        for s in prev_list:
            curr_list.append(s)
            curr_list.append(s+string[0])
        return [s for s in curr_list if all(c in ['a','c','t'] for c in s)]

def test_valid_substrings():
    assert valid_substrings("python")==['py','yt','th','ho']

test_valid_substrings()

"""
Given a list of strings, find all the unique substrings of the strings.
The strings in the