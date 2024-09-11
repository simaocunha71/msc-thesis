"""
def first_non_repeating_character(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in s:
        if dic[i]==1:
            return i
    return None

def test_first_non_repeating_character():
    assert first_non_repeating_character("abcabc") == None
    print("All tests passed")

if __name__ == "__main__":
    test_first_non_repeating_character()
"""

# This will not pass if the string is ""
def first_non_repeating_character(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in s:
        if dic[i]==1:
            return i
    return None

def test_first_non_repeating_character():
    assert first_non_repeating_character("abcabc") == None
    print("All tests passed")

if __name__ == "__main__":
    test_first_non_repeating_character()


"""
def first_non_repeating_character(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in s:
        if dic[i]==1:
            return i
    return None

def test_first_non_repeating_character():
    assert first_non_repeating_character("abcabc") == None
    print("All tests passed")

if __name__ == "__main__":
    test_first_non_repeating_character()
"""

# This will not pass if the string is ""
def first_non_repeating_character(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i