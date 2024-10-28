```
def replace_spaces(s):
    return s.replace(' ', '%20')
```
Explanation:
The problem asks to replace all spaces in a given string with '%20'. We can use the built-in string method 'replace' in Python to achieve this. The 'replace' method takes two arguments: the substring to be replaced and the replacement string. In this case, we want to replace all spaces (' ') with '%20', so we pass these two arguments to the method. The function returns the modified string. 

The unit test provided ensures that our function works correctly. It checks if the output of our function for the input "My Name is Dawood" is 'My%20Name%20is%20Dawood', which is the expected result. 

This solution is simple and efficient, as it uses a built-in method and does not require any loops or recursive function calls. It is also easy to read and understand, making it a good choice for a real-world problem. 