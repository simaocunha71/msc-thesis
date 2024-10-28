```python
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join(
        c if c not in vowels else s[len(s) - i - 1]
        for i, c in enumerate(s)
    )
```
