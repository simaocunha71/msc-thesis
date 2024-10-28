```javascript
const sumSquares = (lst) => {
  return Math.round(lst.map(Math.ceil).map(x => x ** 2).reduce((a, b) => a + b, 0));
}
```
Explanation:
The function `sumSquares` takes a list of numbers as an argument and returns the sum of the squared numbers in the list, with each element rounded to the upper integer using the `Math.ceil` function.

Here's how it works:

1. `lst.map(Math.ceil)`: This part maps each element in the list to its ceiling using the `Math.ceil` function. This rounds each element up to the nearest integer.
2. `lst.map(x => x ** 2)`: This part maps each element in the list to its square using the `**` operator.
3. `reduce((a, b) => a + b, 0)`: This part reduces the list of squared numbers to a single value, which is the sum of all the squared numbers. The initial value of the accumulator is set to 0.

The `Math.round` function is used to round the final result to the nearest integer.

For example, if the input list is `[1, 2, 3]`, the function will first round each element to its ceiling: `[2, 3, 3]`. Then, it will square each element: `[4, 9, 9]`. Finally, it will sum up the squared numbers: `4 + 9 + 9 = 22`. The `Math.round` function will then round the result to the nearest integer, which is `22`. Therefore, the output will be `22`.