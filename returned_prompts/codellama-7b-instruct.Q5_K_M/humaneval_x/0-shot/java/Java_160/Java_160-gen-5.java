        int[] operandArray = new int[operand.size()];
        for (int i = 0; i < operand.size(); i++) {
            operandArray[i] = operand.get(i);
        }

        // 1. evaluate the expression from right to left
        int index = operandArray.length - 1;
        int result = operandArray[index];
        for (int i = index - 1; i >= 0; i--) {
            switch (operator.get(i)) {
                case "+":
                    result += operandArray[i];
                    break;
                case "-":
                    result -= operandArray[i];
                    break;
                case "*":
                    result *= operandArray[i];
                    break;
                case "/":
                    result /= operandArray[i];
                    break;
                case "**":
                    result **= operandArray[i];
                    break;
            }
        }

        return result;
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given two lists operator, and operand. The first list has basic algebra operations, and
    the second list is a list of integers. Use the two given lists to build the algebric
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( / )
    Exponentiation ( ** )

    Example:
    operator["+", "*", "-"]
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
     */
    public int doAlgebra(List<String> operator, List<Integer> oper