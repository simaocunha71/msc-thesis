def check_palindrome_ignore_space(string):
    # your code goes here
    string=string.replace(" ", "")
    for i in string:
        if i not in ".,;:!?":
            return string == string[::-1]

def test_check_palindrome_ignore_space():
    assert check_palindrome_ignore_space("racecar")==True
    assert check_palindrome_ignore_space("hello")==False

test_