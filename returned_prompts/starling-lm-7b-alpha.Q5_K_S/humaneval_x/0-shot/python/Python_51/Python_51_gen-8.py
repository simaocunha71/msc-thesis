

def remove_vowels(text):
    vowels = "aeiou"
    return "".join(ch for ch in text if ch not in vowels)


# Testing
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'


# Other solutions
def remove_vowels(s):
    return s.translate(str.maketrans('', '', "aeiouAEIOU"))


def remove_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    return ''.join([i for i in s if i not in vowels])


# More test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
print(remove_vowels("hello"))  # 'hll'
print(remove_vowels("world"))  # 'wrld'
print(remove_vowels("Hello"))  # 'Hll'
print(remove_vowels("World"))  # 'Wrld'

```

The `remove_vowels` function takes a string as input and returns a new string with all the vowels removed. It does this by using a list comprehension to iterate over each character in the input string and only including the characters that are not in the `vowels` list