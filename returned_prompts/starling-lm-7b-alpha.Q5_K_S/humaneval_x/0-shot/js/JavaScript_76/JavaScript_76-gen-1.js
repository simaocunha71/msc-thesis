To solve this problem, you can follow these steps:

1. Initialize a variable `i` to `1`. This variable will be used to store the value of `n` raised to the power of `j`.
2. Initialize a variable `result` to `false`. This variable will be used to store the result of the function.
3. Use a while loop to iterate until `i` is less than `x`.
4. Inside the loop, check if `i` is equal to `x`. If it is, assign `true` to the `result` variable and break the loop.
5. If `i` is not equal to `x`, calculate the value of `n` raised to the power of `i` by using the exponentiation operator (`**`) and store it in a variable called `power`.
6. Check if `power` is equal to `x`. If it is, assign `true` to the `result` variable and break the loop.
7. If `power` is not equal to `x`, increment the `i` variable by `1`.
8. After the loop, return the `result` variable.

Here's an example implementation of the solution in JavaScript:

```javascript
const isSimplePower = (x, n) => {
  let i = 1;
  let result = false;

  while (i < x) {
    const power = n ** i;
    if (power === x) {
      result = true;
      break;
    }
    i++;
  }

  return result;
};
```

This implementation uses a while loop to iterate until `i` is less than `x`. Inside the loop, it calculates the value of `n` raised to the power of `i` and checks if it is equal to `x`. If it is, it assigns `true` to the `result` variable and breaks the loop. If it's not, it increments the `i` variable by `1`. After the loop, it returns the `result` variable, which will be `true` if `x` is a simple power of `n`, and `false` otherwise.

You can test this function by calling it with different values for `x` and `n` to see if it correctly identifies whether `