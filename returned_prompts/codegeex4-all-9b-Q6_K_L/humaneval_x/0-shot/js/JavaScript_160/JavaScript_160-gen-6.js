You can use the reduce() method to solve this problem. The reduce() method applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value.

Here is the JavaScript solution:

```javascript
const doAlgebra = (operator, operand) => {
  return operator.reduce((acc, curr, i) => {
    if (curr === '+') {
      return acc + operand[i];
    } else if (curr === '-') {
      return acc - operand[i];
    } else if (curr === '*') {
      return acc * operand[i];
    } else if (curr === '//') {
      return Math.floor(acc / operand[i]);
    } else if (curr === '**') {
      return acc ** operand[i];
    } else {
      return acc;
    }
  }, operand[0]);
};
```

This function takes two arguments: operator and operand. It creates a reduce function with an initial value of the first operand. It then iterates over the operators and applies the corresponding operation to the accumulator and the current operand. Finally, it returns the result. 

Note that the floor division operator (//) in JavaScript returns a floating-point number. If you want to get an integer result, you should use Math.floor().