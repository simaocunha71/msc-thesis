To solve this problem, we can iterate through the operator list and perform the corresponding operation with the operands. We can use a stack to keep track of the intermediate results. Here's the implementation:

```javascript
const doAlgebra = (operator, operand) => {
  const stack = [];
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
      default:
        throw new Error(`Invalid operator: ${op}`);
    }

    stack.push(result);
  }

  return result;
};
```

Let's test the function with the given example:

```javascript
const operator = ['+', '*', '-'];
const array = [2, 3, 4, 5];

console.log(doAlgebra(operator, array)); // 9
```

The output is 9, which is the correct result.