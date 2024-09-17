```
import re

def check_str(s):
    if re.match('^[aeiouAEIOU].*', s):
        return True
    else:
        return False
```
The function `check_str` takes a string `s` as an argument and checks whether the string starts with a vowel or not using regular expression. The regular expression `'^[aeiouAEIOU].*'` matches any string that starts with a vowel (both lowercase and uppercase) followed by any characters. The `re.match` function returns a match object if the string matches the regular expression, otherwise it returns `None`. The function then checks if the match object is truthy or not. If it is truthy, it returns `True`, otherwise it returns `False`.

The unit test `assert check_str("annie")` passes because the string "annie" starts with the letter "a" which is a vowel. The function will return `True` for this test case. 

This function is case-insensitive, meaning it treats both lowercase and uppercase vowels as vowels. For example, it will return `True` for both "annie" and "Annie".  If you want to make the function case-sensitive, you can replace the regular expression `'^[aeiouAEIOU].*'` with `'^[aeiou].*'`. This will only match lowercase vowels.  If you want to make the function case-sensitive and treat uppercase vowels as non-vowels, you can replace the regular expression `'^[aeiouAEIOU].*'` with `'^[aeiou].*'`. This will only match lowercase vowels.  If you want to make the function case-sensitive and treat uppercase vowels as vowels, you can replace the regular expression `'^[aeiouAEIOU].*'` with `^[AEIOUaeiou].*` and then return `True` only if the match object is not `None`.  For example:

```
def check_str(s):
    if re.match('^[AEIOUaeiou].*', s):
        return True
    else:
        return False
```  This function will return `True` only if the string starts with a vowel and the vowel is uppercase. It will return `False` for strings that start with lowercase vowels.  This function will also return `False` for strings that do not start with a vowel.  For example, it will return `False` for "hello".  This function is case-sensitive.  If you want to make it case-insensitive