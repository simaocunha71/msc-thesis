```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(0, len(s), 3):
        sub_str = s[i:i+3]
        if len(set(sub_str)) != 3:
            return False
    return True
```


Explanation:
The function is_happy(s) checks if the string s is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

The function first checks if the length of the string is less than 3. If it is, the function returns False because a string with a length less than 3 cannot be happy.

Then, the function iterates over the string in steps of 3 using a for loop. For each iteration, it extracts a substring of length 3 from the original string using slicing.

The function then converts the substring into a set, which automatically removes any duplicate characters. If the length of the set is not equal to 3, it means that the substring has duplicate characters, so the function returns False.

If the function does not return False after checking all substrings of length 3, it means that every 3 consecutive letters are distinct, so the function returns True. This indicates that the string is happy.