```js
const doAlgebra = (operator, operand) => {
    let result = operand[0];
    for (let i = 0; i < operator.length; i++) {
        if (operator[i] === '+') {
            result += operand[i + 1];
        } else if (operator[i] === '-') {
            result -= operand[i + 1];
        } else if (operator[i] === '*') {
            result *= operand[i + 1];
        } else if (operator[i] === '//') {
            result = Math.floor(result / operand[i + 1]);
        } else if (operator[i] === '**') {
            result **= operand[i + 1];
        }
    }
    return result;
};
```
