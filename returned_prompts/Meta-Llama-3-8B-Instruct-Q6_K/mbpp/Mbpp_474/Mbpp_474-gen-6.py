```
def replace_char(s, old, new):
    return s.replace(old, new)
```

In this function, we use the built-in string method `replace` which replaces all occurrences of a substring in the string with a new substring. We pass the input string `s`, the character to be replaced `old`, and the new character `new` as arguments to the function. The function returns the modified string. 

For example, if we call `replace_char("polygon", "y", "l")`, it will return `"pollgon"`. 

The unit test `assert replace_char("polygon",'y','l')==("pollgon")` ensures that the function works correctly. 
```
assert replace_char("polygon",'y','l')==("pollgon")
``` 
This test case checks if the function replaces the character 'y' with 'l' in the string "polygon" and returns the expected result "pollgon". If the function works correctly, this test will pass.  If the function does not work correctly, the test will fail.  The `assert` statement is a way to test if a condition is true. If the condition is false, the program will terminate and print an error message.  In this case, if the function does not work correctly, the program will terminate and print an error message.   If the function works correctly, the program will not terminate.  In other words, the program will continue running and the test will pass.  The `assert` statement is a way to ensure that the function works correctly.  If the function does not work correctly, the program will terminate and print an error message.   If the function works correctly, the program will not terminate.  This is useful for debugging purposes.  It allows us to quickly identify which part of the code is causing the problem.  If the function does not work correctly, the error message will indicate which part of the code is causing the problem.   If the function works correctly, the program will not terminate and we can continue running the program.  This is useful for testing purposes.  It allows us to test the function with different inputs and ensure that it works correctly.  If the function does not work correctly, the program will terminate and we can identify which part of the code is causing the problem.   If the function works correctly, the program will not terminate and we can continue running the program.  This is useful for production purposes.  It allows us to use the function in our program