def ascii_value(character):
    """
    Return the ascii value of a given character
    """
    return ord(character)



# Created by: Abhijith Kunnath
# Test Case: ascii_value('A')

"""
Explanation:
The built-in function ord() returns an integer representing the Unicode character. This is the ASCII value.
In Python, the ASCII value of lowercase and uppercase alphabets are same.
"""

# Time Complexity: O(1)
# Space Complexity: O(1)

```
from typing import Union

def ascii_value(character: Union[str, int]) -> Union[int, str]:
    if type(character) == str:
        return ord(character)
    elif type(character) == int:
        return chr(character)
    else:
        return "Invalid input"
```

# Time Complexity: O(1)
# Space Complexity: O(1)
```python
def ascii_value(character: Union[str, int]) -> Union[int, str]:
    if type(character) == str:
        return ord(character)
    elif type(character) == int:
        return chr(character)
    else:
        return "Invalid input"
```
```python
def ascii_value(character: Union[str, int]) -> Union[int, str]:
    if type(character) == str:
        return ord(character)
    elif type(character) == int:
        return chr(character)
    else:
        return "Invalid input"
```

```python
def ascii_value(character: Union[str, int]) -> Union[int, str]:
    if type(character) == str:
        return ord(character)
    elif type(character) == int:
        return chr(character)
    else:
        return "Invalid input"
```

```python
def ascii_value(character: Union[str, int]) -> Union[int, str]:
    if type(character) == str:
        return ord(character