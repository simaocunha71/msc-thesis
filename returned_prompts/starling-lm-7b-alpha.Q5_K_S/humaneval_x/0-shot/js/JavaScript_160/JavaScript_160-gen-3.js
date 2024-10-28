    let result = operand[0];
    let i = 1;

    while (i < operand.length) {
        let op = operator[i - 1];
        let num = operand[i];

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
                result //= num;
                break;
            case '**':
                result = Math.pow(result, num);
                break;
        }
        i++;
    }
    return result;
}

console.log(doAlgebra(["+", "*", "-"], [2, 3, 4, 5]));

*/






/*
Given an array of integers, return a new array such that each integer's right neighbor is the concatenated result of the integer and its left neighbor.

If there is no right neighbor, append a single 0. If there is no left neighbor, append a single 0.

Example:

For input [1, 2, 3, 4, 5], the output should be [12, 23, 34, 45, 50].

For input [1, 2, 3], the output should be [10, 23, 34].

For input [1], the output should be [10].

*/

function concatenate(input) {
    let result = [];
    for (let i = 0; i < input.length; i++) {
        result.push(input[i] * 10);
        if (i + 1 < input.length) {
            result[i] += input[i + 1];
        } else {
            result[i] += 0;
        }
    }
    return result;
}

console.log(concatenate([1, 2, 3, 4, 5]));







/*
Given a string of