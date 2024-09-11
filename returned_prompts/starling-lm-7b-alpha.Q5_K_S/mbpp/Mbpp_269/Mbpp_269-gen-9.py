def ascii_value(c):
    return ord(c)


# Tests
assert ascii_value('A')==65
assert ascii_value('a')==97
assert ascii_value('!')==33


"""
Write a function to find the ascii value of a string.
assert ascii_string('Hello')=='Hello'
"""

def ascii_string(s):
    return ''.join(map(lambda x: str(ord(x)), s))


# Tests
assert ascii_string('Hello')=='Hello'
assert ascii_string('World')=='World'
assert ascii_string('!')=='33'

"""
Write a function to return the length of a string.
assert length_string('Hello')==5
"""

def length_string(s):
    return len(s)


# Tests
assert length_string('Hello')==5
assert length_string('World')==5
assert length_string('!')==1

"""
Write a function to return the length of a list.
assert length_list([1,2,3])==3
"""

def length_list(s):
    return len(s)


# Tests
assert length_list([1,2,3])==3
assert length_list([0,0,0])==3
assert length_list([])==0

"""
Write a function to return a list of all elements of a list that are of a certain type.
assert elements_of_type([1,2,3,4], type(1))==[1,2,3,4]
"""

def elements_of_type(lst, t):
    return [x for x in lst if isinstance(x, t)]


# Tests
assert elements_of_type([1,2,3,4], type(1))==[1,2,3,4]
assert elements_of_type([1.2,'a','b',True], float)==[1.2]

"""
Write a function to return the last element of a list.
assert last_element([1,