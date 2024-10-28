        int result = operand.get(0);
        for (int i = 1; i < operand.size(); i++) {
            String op = operator.get(i - 1);
            int num = operand.get(i);

            switch (op) {
                case "+":
                    result += num;
                    break;
                case "-":
                    result -= num;
                    break;
                case "*":
                    result *= num;
                    break;
                case "/":
                    result /= num;
                    break;
                case "**":
                    result = (int)Math.pow(result, num);
                    break;
                default:
                    throw new IllegalArgumentException("Invalid operator: " + op);
            }
        }
        return result;
    }
}

The solution uses a simple for loop to iterate over the operand list from the second element to the end. The operator list is used to determine the operation to apply to the current result and the next number in the operand list. The result is updated accordingly.

In the switch statement, "+" adds the number to the result, "-" subtracts the number from the result, "*" multiplies the result by the number, "/" performs floor division of the result by the number, and "**" raises the result to the power of the number. If an invalid operator is encountered, an IllegalArgumentException is thrown.

The final result is returned after all numbers have been processed.

This solution assumes that the operand list and operator list are of the same length and that the operator list is one character long. If this is not the case, the solution needs to be modified to handle different lengths or different formats of operators.
