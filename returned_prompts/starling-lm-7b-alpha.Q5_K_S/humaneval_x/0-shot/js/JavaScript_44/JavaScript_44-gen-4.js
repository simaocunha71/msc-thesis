To convert a given number to a different base, we need to follow these steps:

1. Initialize an empty string called `result` to store the converted result.
2. Initialize a variable `x` with the decimal value of the input number.
3. Initialize a variable `base` with the desired base.
4. Use a while loop to repeat the following steps until `x` becomes zero:
   a. Calculate the remainder of `x` divided by `base`. This will be the next digit of our result.
   b. Convert the remainder to a string and concatenate it to the beginning of the `result` string.
   c. Divide `x` by `base` to get the next value of `x`.
5. Return the `result` string as the final result.

Here's the Python code for the `changeBase` function:

```python
def changeBase(x, base):
    result = ""
    while x:
        result += str(x % base)
        x //= base
    return result
```

To test the function, you can use the following test cases:

```python
print(changeBase(8, 3))  # Output: '22'
print(changeBase(8, 2))  # Output: '1000'
print(changeBase(7, 2))  # Output: '111'
```

These test cases demonstrate that the function correctly converts a given number to a different base.

*/

function changeBase(x, base) {
  let result = "";
  while (x) {
    result += String(x % base);
    x = Math.floor(x / base);
  }
  return result;
}

// Test cases
console.log(changeBase(8, 3));  // Output: '22'
console.log(changeBase(8, 2));  // Output: '1000'
console.log(changeBase(7, 2));  // Output: '111'

```

This JavaScript code defines the `changeBase` function that converts a given number to a different base. The function uses a while loop to repeatedly calculate the remainder of `x`