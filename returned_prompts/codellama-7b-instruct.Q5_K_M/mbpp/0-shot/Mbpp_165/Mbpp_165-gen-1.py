```
def count_char_position(s):
    return sum(1 for c in s if c.lower() == chr((ord(c.lower()) - ord('a') + 13) % 26 + ord('a')).lower())
```
