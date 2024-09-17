You can use list comprehension and the built-in function `list()` to split a string into characters. Here is the function:

```python
def split(s):
    return list(s)
```

This function works by directly converting the string `s` into a list of characters. The unit test `assert split('python') == ['p','y','t','h','o','n']` ensures that the function is working correctly.  If you want to ensure that the function works for any string, you can use the following unit test:

```python
assert split('python') == ['p','y','t','h','o','n']
assert split('') == []
assert split('a') == ['a']
assert split('abc') == ['a', 'b', 'c']
```  These tests cover the cases of an empty string, a single character string, and a string with multiple characters.  The function will pass all these tests as long as it correctly splits any string into characters.  You can add more tests as needed to cover edge cases.  



The function is simple and works correctly as long as the input is a string. It does not handle other types of input, so you may want to add error checking code if you expect to be passing other types of input to the function. For example, you might add a check at the beginning of the function to raise an error if the input is not a string:

```python
def split(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return list(s)
```  This code will raise an error if the input is not a string, which can help prevent errors and make the function more robust.  However, this is just one possible way to handle the case where the input is not a string.  You might choose to handle this case differently depending on your needs.  



The function does not modify the input string, it returns a new list.  This is a good design choice because it means that the function is pure and does not have any side effects.  It also makes the function easier to use because it does not modify the original string.  For example, you can use the function like this:

```python
original_string = 'python'
characters = split(original_string)
print(characters)  # prints ['p', 'y', 't', 'h', 'o', 'n']
print(original_string)  # still prints 'python'
```  As you