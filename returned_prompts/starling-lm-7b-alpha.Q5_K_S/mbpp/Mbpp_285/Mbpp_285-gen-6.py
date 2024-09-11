def text_match_two_three(string):
    if len(string)<3:
        return False
    if string[0]=='a' and string[1]=='b' and string[2]=='b':
        return True
    if string[0]=='a' and string[1]=='b' and string[2]=='c':
        return True
    else:
        return False


# Another way:
def text_match_two_three_2(string):
    if len(string)<3:
        return False
    if "ab" in string and "bb" in string:
        return True
    else:
        return False


# Another way:
def text_match_two_three_3(string):
    if len(string)<3:
        return False
    return (string[0]=='a' and string[1]=='b' and string[2]=='b') or (string[0]=='a' and string[1]=='b' and string[2]=='c')


"""
It's important to note that, if the string is too long, it may take up a lot of memory,
so we should consider the length of the string while designing the function.
"""

# Your code contributions are licensed under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).


def text_match_two_three(string):
    if len(string)<3:
        return False
    if string[0]=='a' and string[1]=='b' and string[2]=='b':
        return True
    if string[0]=='a' and string[1]=='b' and string[2]=='c':
        return True
    else:
        return False

# Another way:
def text_match_two_three_2(string):
    if len(string)<3:
        return False
    if "ab" in string and "bb" in string:
        return True
    else:
        return False

# Another way:
def text_match_two_three