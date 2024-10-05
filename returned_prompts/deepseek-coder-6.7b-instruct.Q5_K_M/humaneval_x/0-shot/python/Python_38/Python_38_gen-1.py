

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # un-cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


if __name__ == "____main__":
    test_str = "Hello, World!"
    print(f"Original string: {test_str}")

    encoded_str = encode_cyclic(test_str)
    print(f"Encoded string: {encoded_str}")

    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")

    assert test_str == decoded_str, f"Error: {test_str} != {decoded_str}"

# This program will print:
# Original string: Hello, World
# Encoded string: elHlo,Wlord
# Decoded string: Hello, World
# If there are no assertions raised, it means that the encode_cyclic and decode_cyclic functions work correctly.

```

## 3.2

### Code

```python
def is_palindrome(s: str):
    """
    returns True if string is a palindrome and False otherwise.
    """
    return s == s[::-1]


def is_anagram(s: str, t: str):
    """
    returns True if strings are anagrams and False otherwise.
    """
    return sorted(s) == sorted(t)


def is_pangram(s: str, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
   