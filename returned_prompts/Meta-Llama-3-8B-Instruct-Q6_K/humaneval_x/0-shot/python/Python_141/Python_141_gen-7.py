```
def file_name_check(file_name):
    if len([char for char in file_name if char.isdigit()]) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not file_name.split('.')[0][0].isalpha():
        return 'No'
    if file_name.split('.')[1].lower() not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
```


Explanation:
The function `file_name_check(file_name)` takes a string representing a file's name as input. It checks the file's name according to the given conditions and returns 'Yes' if the name is valid, and 'No' otherwise.

1. The function first checks if there are more than three digits in the file's name. It does this by creating a list comprehension that includes all characters in the file's name that are digits, and then checks if the length of this list is greater than 3. If it is, the function returns 'No'.

2. Then, the function checks if the file's name contains exactly one dot. It does this by using the `count()` method of the string, which returns the number of occurrences of the specified character (in this case, the dot). If the count is not equal to 1, the function returns 'No'.

3. Next, the function checks if the substring before the dot starts with a letter from the latin alphabet. It does this by splitting the file's name into two substrings at the dot, and then checking if the first character of the first substring is a letter using the `isalpha()` method. If it is not, the function returns 'No'.

4. Finally, the function checks if the substring after the dot is one of the allowed extensions ('txt', 'exe', 'dll'). It does this by splitting the file's name into two substrings at the dot, and then checking if the second substring (converted to lowercase) is one of the allowed extensions using a list comprehension. If it is not, the function returns 'No'.

5. If all the conditions are met, the function returns 'Yes'. Otherwise, it returns 'No'.