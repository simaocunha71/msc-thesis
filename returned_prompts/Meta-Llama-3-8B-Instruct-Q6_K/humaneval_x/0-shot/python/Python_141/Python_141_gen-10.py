```
def file_name_check(file_name):
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    if not parts[0][0].isalpha():
        return 'No'
    if not all(c.isalnum() or c.isspace() for c in parts[0][1:]):
        return 'No'
    if len([c for c in parts[0] if c.isdigit()]) > 3:
        return 'No'
    if parts[1].lower() not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
```


This function splits the file name into two parts at the dot. It checks if the first part starts with a letter from the latin alphabet and if there are no more than three digits in this part. It also checks if the second part is one of the allowed extensions. If all these conditions are met, it returns 'Yes', otherwise 'No'. 

The function uses the following built-in Python functions:
- `split`: splits a string into a list of substrings.
- `isalpha`: checks if a character is a letter from the latin alphabet.
- `isalnum`: checks if a character is a letter or a digit.
- `isspace`: checks if a character is a whitespace character.
- `isdigit`: checks if a character is a digit.
- `lower`: converts a string to lowercase. 
- `all`: checks if all elements in an iterable are true. 
- `len`: returns the length of a string or a list. 
- `return`: returns a value. 







Please let me know if you have any questions or need further clarification.