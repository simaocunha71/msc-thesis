Here is a JavaScript function that does what you described:
```
const sumSquares = (lst) => {
  return lst.map(Math.ceil).map(x => x ** 2).reduce((a, b) => a + b, 0);
};
```
Here's an explanation of how the function works:

1. `lst.map(Math.ceil)`: This uses the `map` method to apply the `Math.ceil` function to each element in the list. This rounds each element up to the nearest integer.
2. `map(x => x ** 2)`: This uses another `map` method to square each element in the list.
3. `reduce((a, b) => a + b, 0)`: This uses the `reduce` method to sum up all the squared elements. The initial value of the accumulator is 0.

You can test the function with the examples you provided:
```
console.log(sumSquares([1, 2, 3])); // 14
console.log(sumSquares([1, 4, 9])); // 98
console.log(sumSquares([1, 3, 5, 7])); // 84
console.log(sumSquares([1.4, 4.2, 0])); // 29
console.log(sumSquares([-2.4, 1, 1])); // 6
```
I hope this helps! Let me know if you have any questions.