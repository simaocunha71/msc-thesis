```
def replace_blank(s, c):
    return s.replace(" ", c)
```



The problem is asking you to create a function that takes a string and a character as input. The function should replace all blank spaces in the string with the given character and return the modified string.

The unit test `assert replace_blank("hello people",'@')==("hello@people")` helps to clarify the problem by showing that the function should replace all blank spaces with the given character.

Here is the solution:
```
def replace_blank(s, c):
    return s.replace(" ", c)
```
This function uses the `replace` method of the string, which replaces all occurrences of the first argument (in this case, " ") with the second argument (in this case, c). The modified string is then returned.