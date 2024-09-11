def sub_list(list1,list2):
    return [i-j for i,j in zip(list1,list2)]

def test_sub_list():
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]

test_sub_list()








"""
Given a list of strings, return a list of lists where the first list contains all of the strings with an even length, and the second list contains all of the strings with an odd length.
assert separate_even_odd(['a','bc','d','efg','hij'])==(['a', 'bc', 'd', 'hij'], ['efg'])
"""

def separate_even_odd(list_str):
    return ([i for i in list_str if len(i) % 2 == 0], [i for i in list_str if len(i) % 2 != 0])

def test_separate_even_odd():
    assert separate_even_odd(['a','bc','d','efg','hij'])==(['a', 'bc', 'd', 'hij'], ['efg'])

test_separate_even_odd()

"""
Given a list of strings, return a list of strings with all of the strings in uppercase.
assert upper_case(['a','bc','d'])==(['A', 'BC', 'D'])
"""

def upper_case(list_str):
    return [i.upper() for i in list_str]

def test_upper_case():
    assert upper_case(['a','bc','d'])==(['A', 'BC', 'D'])

test_upper_case()

"""
Given a list of strings, return a list of strings with all of the strings in lowercase.
assert lower_case(['A','BC','D'])==(['a', 'bc', 'd'])
"""

def lower_case(list_str):
    return [i.lower() for i in list_str]

def test_lower_case():
    assert lower_case(['A','BC','D'])==(['a', 'bc', 'd'])

