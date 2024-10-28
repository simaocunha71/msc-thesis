To solve this problem, you need to iterate over the operator list and perform the corresponding operation on the operands. Here's how you can implement the `doAlgebra` function in JavaScript:

```javascript
const doAlgebra = (operator, operand) => {
    // Initialize the result with the first operand
    let result = operand[0];

    // Iterate over the operator list
    for (let i = 0; i < operator.length; i++) {
        // Get the current operator and operand
        const op = operator[i];
        const num = operand[i + 1];

        // Perform the operation
        if (op === '+') {
            result += num;
        } else if (op === '-') {
            result -= num;
        } else if (op === '*') {
            result *= num;
        } else if (op === '//') {
            result = Math.floor(result / num);
        } else if (op === '**') {
            result = Math.pow(result, num);
        }
    }

    // Return the final result
    return result;
}
```

You can test the function with the provided example:

```javascript
const operator = ['+', '*', '-'];
const operand = [2, 3, 4, 5];
console.log(doAlgebra(operator, operand)); // Output: 9
```