```
def remove_uppercase(s):
    return ''.join(c for c in s if c.islower())
```
This function uses a generator expression to iterate over each character `c` in the input string `s`. The `islower()` method checks if a character is lowercase, and if it is, it is included in the resulting string. The `join()` method is used to concatenate the characters into a single string. 

For example, if the input string is 'cAstyoUrFavoRitETVshoWs', the function will return 'cstyoravoitshos', which is the string with all uppercase characters removed. 

This solution passes the given unit test:
```
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
``` 