        int result = operand.get(0);
        for (int i = 1; i < operand.size(); i++) {
            String op = operator.get(i-1);
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
            }
        }
        return result;
    }
}

The program takes a list of operators and a list of integers, and evaluates the expression using the two lists. The evaluation starts from the first integer and continues with the rest of the numbers. Each number is combined with the previous number using the operator before it.

This solution assumes that the operand list will always be a list of integers and the operator list will always be a list of strings. It also assumes that the operator list will always have one less element than the operand list.

It uses a for loop to iterate through the operand list, starting from the second element. For each element in the operand list, it gets the corresponding operator from the operator list and applies the operation to the result and the current number.

The operation is determined by a switch statement, which matches the operator string and applies the corresponding operation to the result and the number. The result of this operation becomes the new result for the next iteration.

After all the numbers have been processed, the final result is returned.

The program uses the Java programming language. It uses the Java standard library, so no additional libraries are needed.

The time complexity of the program is O(n), where n is the length of the operand list. This is because it performs a constant amount of work for each element in the operand list.

The space complexity of the program is O(1), because it only uses a constant amount of space to store the result and the variables used for iteration. The space complexity does not include the space needed for the input lists, which are not considered part of the solution.

Test cases:

