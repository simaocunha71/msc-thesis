"""
You can solve this problem as follows:

```python
def move_num(s):
    nums = ''
    res = ''
    for char in s:
        if char.isdigit():
            nums += char
        else:
            res += char
    return res + nums
```"""

This solution works by iterating over the input string and separating the non-numeric characters into one string and the numeric characters into another. Finally, it returns the string of non-numeric characters followed by the string of numeric characters. The unit test provided ensures that the function works correctly. For example, when called with the string "I1love143you55three3000thousand", the function returns "Iloveyouthreethousand1143553000".