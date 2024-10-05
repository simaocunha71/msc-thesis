```
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}
```



Explanation:

*   The function `sumToN` takes an integer `n` as input.
*   It initializes a variable `sum` to 0, which will be used to store the sum of numbers from 1 to `n`.
*   It uses a `for` loop to iterate from 1 to `n` (inclusive).
*   Inside the loop, it adds each number `i` to the `sum` variable.
*   Finally, it returns the `sum` value.

This implementation has a time complexity of O(n) and a space complexity of O(1), as it only uses a constant amount of space to store the `sum` variable.