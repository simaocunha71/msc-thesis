```
def remove_whitespaces(s):
    return s.replace(" ", "")
```


The unit test `assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'` helps to clarify that the function should remove all whitespaces from the given string. 

The solution uses the `replace` method of the string, which replaces all occurrences of the given substring (in this case, a single whitespace character) with an empty string. This effectively removes all whitespaces from the string. 

Note that this solution assumes that the problem wants to remove all types of whitespace characters, not just spaces. If it's meant to only remove spaces, you can use the `replace(' ', '')` method. If you want to remove all types of whitespace characters, you can use the `replace('\s', '')` method. 

Here is the code with the test:

```
def remove_whitespaces(s):
    return s.replace(" ", "")

assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
``` 





