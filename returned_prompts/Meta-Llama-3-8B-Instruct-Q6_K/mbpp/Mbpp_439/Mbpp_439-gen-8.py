You can use the built-in `int` function in Python, which can convert a string to an integer. You can use the `join` function to concatenate the strings representation of each integer in the list, and then convert the result to an integer.

Here is a Python function that does this:

```
def multiple_to_single(lst):
    return int(''.join(map(str, lst)))
```

This function works by using the `map` function to convert each integer in the list to a string, then using the `join` function to concatenate these strings together. The result is a string that is the concatenation of the strings representation of each integer in the list. This string is then converted to an integer using the `int` function.

For example, if you call `multiple_to_single([11, 33, 50])`, the function will return `113350`, which is the concatenation of the strings representation of each integer in the list. This is the desired output. 

The unit test `assert multiple_to_single([11, 33, 50])==113350` ensures that the function works correctly. If the function returns a different value, the test will fail. 





```
```



```
```



```
```



```
```



```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





```
```





