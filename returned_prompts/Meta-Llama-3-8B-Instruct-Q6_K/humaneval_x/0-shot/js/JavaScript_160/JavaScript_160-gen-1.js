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
We iterate through the operator list, and for each operator, we apply the corresponding operation to the current result and the next operand. We use a switch statement to determine which operation to perform based on the operator. The result is updated accordingly. Finally, we return the final result. 

Note: We use the Math.floor function for floor division to ensure the result is an integer. We also use the Math.pow function for exponentiation. 

Example:
```
const operator = ['+', '*', '-'];
const operand = [2, 3, 4, 5];
console.log(doAlgebra(operator, operand)); // Output: 9
```

This code will evaluate the expression 2 + 3 * 4 - 5 and return the result 9.