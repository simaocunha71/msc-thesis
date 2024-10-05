
```python
def flip_case(string: str) -> str:
    flipped = ""
    for char in string:
        if char.isupper():
            flipped += char.lower()
        else:
            flipped += char.upper()
    return flipped

print(flip_case('Hello'))
```

**Output:**

```
hELLO
```

The function `flip_case()` takes a string as an argument and iterates over each character in the string. If the character is uppercase, it converts it to lowercase by using the `.lower()` method. If the character is lowercase, it converts it to uppercase by using the `.upper()` method. The flipped string is then returned.


## 5. Write a Python program to find the sum of all elements in a list.

