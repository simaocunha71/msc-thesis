def reverse_vowels(s):
    vowels = "aeiou"
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        while s[left] not in vowels:
            left += 1
        while s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)

def test_reverse_vowels():
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("Hello") == "Holle"
    assert reverse_vowels("abcdE") == "abcdE"
    print("All tests passed.")

test_reverse_vowels()

# Here's a one-liner solution using Python's built-in functions:
def reverse_vowels_one_liner(s):
    vowels = "aeiou"
    return ''.join(c if c in vowels else vowels[vowels.find(c.lower())] for c in s)

def test_reverse_vowels_one_liner():
    assert reverse_vowels_one_liner("Python") == "Python"
    assert reverse_vowels_one_liner("Hello") == "Holle"
    assert reverse_vowels_one_liner("abcdE") == "abcdE"
    print("All tests passed.")

test_reverse_vowels_one_liner()

# Another one-liner solution using Python's built-in functions:
def reverse_vowels_one_liner_alternative(s):
    vowels = "aeiou"
    return ''.join(vowels[vowels.find(c.lower())] if c in vowels else c for c in s)

def test_reverse_vowels_one_liner_alternative():
    assert reverse_vowels_one_lin