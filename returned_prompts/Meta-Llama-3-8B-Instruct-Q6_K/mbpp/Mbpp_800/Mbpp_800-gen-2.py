```
def remove_all_spaces(s):
    return s.replace(" ", "")
```


The function `remove_all_spaces` takes a string `s` as input and returns a new string with all the spaces removed. This is achieved by using the `replace` method of the string, which replaces all occurrences of a specified substring with another substring. In this case, we replace all spaces with an empty string, effectively removing them. 

The unit test `assert remove_all_spaces('python  program')==('pythonprogram')` ensures that the function works correctly by comparing the output of the function with the expected output. 

This function is case-sensitive, meaning that it treats uppercase and lowercase letters differently. If you want to treat uppercase and lowercase letters as the same, you would need to convert the string to lowercase or uppercase before removing the spaces. For example:

```
def remove_all_spaces(s):
    return s.lower().replace(" ", "")
```

This function would convert the string to lowercase before removing the spaces, so it would treat 'Python' and 'python' as the same.  If you want to treat uppercase and lowercase letters as the same and also remove punctuation, you could use the following function:

```
import string

def remove_all_spaces(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    return s.replace(" ", "")
```


This function would convert the string to lowercase, remove all punctuation, and then remove all spaces.  The `str.maketrans` function creates a translation table that maps each punctuation character to None, effectively removing it. The `translate` method applies this translation table to the string.  This function would treat 'Python' and 'python' as the same, and it would also remove punctuation, so 'Hello, world!' would become 'helloworld'.  However, it would not remove spaces, so 'Hello world' would still contain a space.  If you want to remove spaces as well, you could use the `replace` method again:

```
import string

def remove_all_spaces(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
    return s
```


This function would convert the string to lowercase, remove all punctuation, and then remove all spaces.  It would treat 'Python' and 'python' as the same, and it would remove both punctuation and spaces.  So 'Hello, world!'