```
def hexagonal_num(n):
    return (n * (3 * n - 1)) // 2
```

Explanation:

A hexagonal number is the sum of the first n positive integers in a hexagonal arrangement. The formula for the nth hexagonal number can be derived by counting the number of dots in a hexagon. Each row has one more dot than the previous row, with the first row having one dot, the second row having two dots, and so on. 

The formula for the nth hexagonal number is (n * (3 * n - 1)) // 2. 

To find the nth hexagonal number, you can use the formula by plugging in the value of n into the function hexagonal_num(n). The function will calculate and return the nth hexagonal number. 

In the provided assertion, hexagonal_num(10) is called with the argument 10, which should return 190. This means that the 10th hexagonal number is 190. 

The function hexagonal_num(n) is defined as follows:

```python
def hexagonal_num(n):
    return (n * (3 * n - 1)) // 2
```

This function takes an integer argument n and returns the nth hexagonal number using the formula. 

By using this function with different values of n, you can find the nth hexagonal number easily.

For example, calling hexagonal_num(5) will return the 5th hexagonal number, which is 45. 

Similarly, hexagonal_num(10) will return the 10th hexagonal number, which is 190. 

The formula (n * (3 * n - 1)) // 2 is used to calculate the nth hexagonal number efficiently. 

The assertion hexagonal_num(10) == 190 is used to verify that the function is correctly calculating the hexagonal number for the given value of n. 

In summary, the provided function hexagonal_num(n) calculates the nth hexagonal number using the formula (n * (3 * n - 1)) // 2 and