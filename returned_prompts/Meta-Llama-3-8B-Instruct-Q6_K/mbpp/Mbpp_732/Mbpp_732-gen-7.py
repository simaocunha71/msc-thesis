```
def replace_specialchar(s):
    return s.replace(" ", ":").replace(",", ":").replace(".", ":")
```


This function uses the `replace` method of the string, which replaces all occurrences of a specified substring with another substring. It first replaces all spaces with a colon, then all commas, and finally all dots. The result is a string where all spaces, commas, and dots have been replaced with a colon.