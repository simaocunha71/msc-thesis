You can solve this problem with the following function:

```python
def replace_specialchar(s):
    s = s.replace(' ', ':')
    s = s.replace(',', ':')
    s = s.replace('.', ':')
    return s
```


This function will replace all the spaces, commas, and dots in the given string with a colon. The unit test provided ensures the correctness of the function. For example, `replace_specialchar('Python language, Programming language.')` will return `'Python:language::Programming:language:'`. 

The time complexity of this function is O(n), where n is the length of the input string. This is because it needs to traverse the string once for each special character. The space complexity is O(n), as it needs to store the resulting string. 

This function is case-sensitive, meaning it will treat uppercase and lowercase letters differently. If you want a case-insensitive function, you can convert the string to lowercase or uppercase before replacing the special characters. However, this is not necessary based on the provided unit test. 

It's also worth noting that this function does not handle non-ASCII characters. If you need to handle non-ASCII characters, you may need to use a more complex solution. 

Finally, this function does not handle Unicode characters. If you need to handle Unicode characters, you may need to use a more complex solution. 

The provided unit test ensures that the function works correctly for the given input. You can add more tests to ensure that the function works correctly for other inputs. 

Here is the complete code:

```python
def replace_specialchar(s):
    s = s.replace(' ', ':')
    s = s.replace(',', ':')
    s = s.replace('.', ':')
    return s

assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
```


You can run this code and it will pass the provided unit test. You can also add more tests to ensure that the function works correctly for other inputs. 