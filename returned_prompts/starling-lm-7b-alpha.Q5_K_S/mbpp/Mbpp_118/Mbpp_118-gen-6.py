def is_substring(str1, str2):
    return str1 in str2

def test_is_substring():
    assert is_substring("hello","world")==True

test_is_substring()

"""
Write a function to take two strings as arguments and return the minimum of the