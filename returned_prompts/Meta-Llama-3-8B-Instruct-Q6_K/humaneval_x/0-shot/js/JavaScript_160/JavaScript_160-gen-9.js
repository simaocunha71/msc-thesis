```
const doAlgebra = (operator, operand) => {
  let result = operand[0];
  for (let i = 0; i < operator.length; i++) {
    const op = operator[i];
    const num = operand[i + 1];
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
      case '//':
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
The function takes two parameters: `operator` and `operand`. The `operator` parameter is an array of strings representing the basic algebra operations, and the `operand` parameter is an array of integers.

The function initializes a variable `result` to the first element of the `operand` array.

It then iterates through the `operator` array, and for each operator, it performs the corresponding operation on the `result` variable and the next element of the `operand` array.

After the loop, the function returns the final value of `result`.

The switch statement is used to determine which operation to perform based on the current operator. The `Math.floor` function is used for floor division, and the `Math.pow` function is used for exponentiation.

The function assumes that the `operator` array has at least one element, and the `operand` array has at least two elements. It also assumes that the operands are non-negative integers. If these assumptions are not met, the function may not work correctly.