"""
def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - ord('a') == i:
            count += 1
    return count
"""

def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - ord('a') == i:
            count += 1
    return count

def test_count_char_position():
    assert count_char_position("xbcefg") == 2
    print("All Test Passed")

test_count_char_position()



# Made By Mostafa_Khaled
```