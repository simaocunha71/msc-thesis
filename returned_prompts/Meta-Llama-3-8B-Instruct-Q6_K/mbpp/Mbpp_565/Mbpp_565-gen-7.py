You can use a list comprehension to achieve this. Here is the solution:
```
def split(s):
    return [char for char in s]
```
This function uses a list comprehension to iterate over each character in the input string `s` and returns a list of those characters. 

For example, if you call `split('python')`, it will return `['p', 'y', 't', 'h', 'o', 'n']`. 

The unit test `assert split('python') == ['p','y','t','h','o','n']` ensures that the function works correctly. 