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
The function `doAlgebra` takes two parameters: `operator` and `operand`. It initializes the result with the first element of the `operand` list. Then, it iterates over the `operator` list. For each operator, it takes the corresponding element from the `operand` list, and based on the operator, it performs the corresponding operation on the result. Finally, it returns the result.

The switch statement is used to determine which operation to perform based on the operator. The `Math.floor` function is used for floor division, and `Math.pow` is used for exponentiation.

For example, if the `operator` list is `['+', '*', '-']` and the `operand` list is `[2, 3, 4, 5]`, the function will perform the following operations:

1. `result = 2 + 3` => `result = 5`
2. `result = 5 * 4` => `result = 20`
3. `result = 20 - 5` => `result = 15`

So, the final result is `15`.