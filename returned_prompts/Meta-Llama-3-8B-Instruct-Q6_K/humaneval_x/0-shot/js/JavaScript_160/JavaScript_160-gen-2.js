```
const doAlgebra = (operator, operand) => {
  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    let op = operator[i];
    let num = operand[i + 1];
    switch (op) {
      case '+':
        result += num;
        break;
      case '-':
        result -= num;
        break;
      case '*':
        result *= num;
        break;
      case '//' :
        result = Math.floor(result / num);
        break;
      case '**':
        result = Math.pow(result, num);
        break;
    }
  }
  return result;
};
```


Explanation:
The function takes two parameters, `operator` and `operand`. The `operator` is a list of basic algebra operations, and the `operand` is a list of integers.

The function initializes a variable `result` with the first element of the `operand` list.

Then, it loops through the `operator` list, and for each operator, it applies the corresponding operation to the `result` and the next element in the `operand` list.

The function uses a `switch` statement to determine which operation to perform based on the current operator.

Finally, the function returns the final value of `result`.