    let result = operand.shift();
    for (let i = 0; i < operator.length; i++) {
        let op = operator[i];
        let right = operand.shift();
        if (op === '+') {
            result += right;
        } else if (op === '-') {
            result -= right;
        } else if (op === '*') {
            result *= right;
        } else if (op === '//') {
            result = Math.floor(result / right);
        } else if (op === '**') {
            result = Math.pow(result, right);
        }
    }
    return result;
};

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5]));
// Explanation:
// Here, the operator list has '+', '*', '-' and the operand list has 2, 3, 4, 5.

// First, we shift the first operand from the list and assign the result to the variable result.
// result = 2

// Then, we iterate through the operator list and perform the corresponding operation on the result
// and the next operand.

// When the op is '+', we add the right operand to the result.
// result = 2 + 3 = 5

// When the op is '-', we subtract the right operand from the result.
// result = 5 - 4 = 1

// When the op is '*', we multiply the result by the right operand.
// result = 1 * 5 = 5

// When the op is '//', we divide the result by the right operand and round down to the nearest whole number.
// result = 5 // 5 = 1

// When the op is '**', we raise the result to the power of the right operand.
// result = 1 ** 5 = 1

// The result is 1, which is the final result of the expression.














































