    const stack = [];
    const ops = new Set(operator);
    for (let i = 0; i < operand.length; i++) {
        if (!ops.has(operator[i])) {
            stack.push(operand[i]);
        } else {
            const b = stack.pop();
            const a = stack.pop();

            switch (operator[i]) {
                case '+':
                    stack.push(a + b);
                    break;
                case '-':
                    stack.push(a - b);
                    break;
                case '*':
                    stack.push(a * b);
                    break;
                case '//':
                    stack.push(Math.floor(a / b));
                    break;
                case '**':
                    stack.push(Math.pow(a, b));
                    break;
                default:
                    break;
            }
        }
    }

    return stack[0];
};

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])); // 9
console.log(doAlgebra(['+', '*'], [2, 3, 4, 5])); // 26















































































































































































































