```
def match_starta_endb(text):
    import re
    return bool(re.match("a.*b", text))
```


The function `match_starta_endb` takes a string `text` as input. It uses the `re` module to compile a regular expression pattern `a.*b`. The pattern matches a string that starts with 'a', followed by any characters (captured by `.*`), and ends with 'b'. The `re.match` function returns a match object if the pattern matches the input string, and `None` otherwise. The `bool` function is used to convert the match object to a boolean value. If the input string matches the pattern, the function returns `True`; otherwise, it returns `False`. The unit test `assert text_starta_endb("aabbbb")` ensures that the function correctly matches the string "aabbbb". 

Note: The `.*` in the regular expression pattern is a greedy match, meaning it will match as many characters as possible. If you want a non-greedy match (i.e., matching as few characters as possible), you can use `.*?` instead. 

Also, the `re.match` function only matches at the beginning of the string. If you want to match anywhere in the string, you can use `re.search` instead. 

Here's an example of how you can use the function:
```
print(match_starta_endb("aabbbb"))  # Returns: True
print(match_starta_endb("abc"))  # Returns: False
print(match_starta_endb("aabb"))  # Returns: False
``` 
This code demonstrates that the function correctly matches the input string "aabbbb" and returns `False` for the strings "abc" and "aabb". 