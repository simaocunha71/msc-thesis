
def find_max(words):
    # Write your solution here
    if len(words) == 0:
        return ""
    max_char = 0
    max_word = ""
    for word in words:
        if len(set(word)) > max_char:
            max_char = len(set(word))
            max_word = word
    return max_word

# Tests

def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["aaaaaaa", "bb" ,"cc", "a"]) == "aaaaaaa"
    assert find_max(["aaaaaaa", "bb" ,"cc", "a", "a"]) == "aaaaaaa"
    assert find_max(["aaaaaaa", "bb" ,"cc", "a", "a", "bb"]) == "aaaaaaa"
    assert find_max(["aaaaaaa", "bb" ,"cc", "a", "a", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["aaaaaaa", "bb" ,"cc", "a", "a", "bb", "cc", "aaaaaaa"]) == "aaaaaaa"
    assert find_max(["aaaaaaa", "bb" ,"cc", "a", "a", "bb", "cc", "aaaaaaa", "bb"]) == "aaaaaaa"

test_find_max()

# Submission

def find_max(words):
    return max(words, key=lambda s: (len(set(s)), s))[1]

