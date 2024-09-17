```
def replace_blank(s, c):
    return s.replace(' ', c)
```  # Replace blank spaces with the given character
```python
assert replace_blank("hello people", '@') == "hello@people"
```  # Test case
```python
replace_blank("hello world", '$')  # Replace blank spaces with $
```  # Example usage
```
The function takes a string `s` and a character `c` as inputs, and returns the string with all blank spaces replaced with the character `c`. The unit test `assert replace_blank("hello people", '@') == "hello@people"` ensures that the function works correctly. The example usage `replace_blank("hello world", '$')` shows how to use the function to replace blank spaces with a different character.