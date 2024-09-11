def remove_all_spaces(string):
    string=string.replace(" ","")
    return string


remove_all_spaces('python  program')




"""
def remove_all_spaces(string):
    string=string.replace(" ","")
    return string

def test_remove_all_spaces():
    assert remove_all_spaces('python  program')=='pythonprogram'
    print("All test cases passed")

test_remove_all_spaces()
"""


"""
def remove_all_spaces(string):
    return "".join(string.split())

def test_remove_all_spaces():
    assert remove_all_spaces('python  program')=='pythonprogram'
    print("All test cases passed")

test_remove_all_spaces()
"""

"""
def remove_all_spaces(string):
    new_string=""
    for i in range(len(string)):
        if string[i]!=" ":
            new_string+=string[i]
    return new_string

def test_remove_all_spaces():
    assert remove_all_spaces('python  program')=='pythonprogram'
    print("All test cases passed")

test_remove_all_spaces()
"""


"""
def remove_all_spaces(string):
    new_string=""
    for i in string:
        if i!=" ":
            new_string+=i
    return new_string

def test_remove_all_spaces():
    assert remove_all_spaces('python  program')=='pythonprogram'
    print("All test cases passed")

test_remove_all_spaces()
"""

"""
def remove_all_spaces(string):
    new_string=""
    for i in range(len(string)):
        if string[i]!=" ":
            new_string+=string[i]
    return new_string

def test_remove_all_spaces():
    assert remove_all_spaces('python  program')=='pythonprogram'
    print("All test cases passed")

test