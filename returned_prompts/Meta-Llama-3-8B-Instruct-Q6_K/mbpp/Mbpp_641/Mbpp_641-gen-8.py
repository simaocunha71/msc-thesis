The nth nonagonal number is given by the formula: (n*(8n-1))/2. This is a mathematical formula that calculates the nth nonagonal number.
Here is the python function that implements this formula:

```
def is_nonagonal(n):
    return (n * (8 * n - 1)) // 2
```
This function takes an integer n as an argument and returns the nth nonagonal number. The `//` operator is used for integer division to ensure that the result is an integer.
The unit test `assert is_nonagonal(10) == 325` ensures that the function is working correctly. This test checks that the 10th nonagonal number is indeed 325. If the function is correct, this test will pass. If the function is incorrect, this test will fail, indicating that the function needs to be corrected. 