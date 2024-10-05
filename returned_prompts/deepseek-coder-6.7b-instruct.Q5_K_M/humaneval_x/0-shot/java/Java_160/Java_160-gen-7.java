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
                    result = (int) Math.pow(result, num);
                    break;
                default:
                    throw new IllegalArgumentException("Invalid operator: " + op);
            }
        }

        return result;
    }
}


A: Here is a version of the code that uses a stack to hold the operands, and a queue to hold the operators. This way, we can follow the order of operations as per the BODMAS rule.

import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        Stack<Integer> stack = new Stack<>();
        Queue<String> queue = new LinkedList<>(operator);

        stack.push(operand.get(0));

        for (int i = 1; i < operand.size(); i++) {
            String op = queue.poll();
            stack.push(operand.get(i));

            if (op.equals("+") || op.equals("-")) {
                while (!stack.isEmpty() && (stack.peek() != Integer.MIN_VALUE)) {
                    stack.push(Integer.MIN_VALUE);
                    int num2 = stack.pop();
                    int num1 = stack.pop();
                    stack.push(op.equals("+") ? num1 + num2 : num1 - num2);
                }
            } else if (op.equals("*") || op.equals("/")) {
                while (!stack.isEmpty() && stack.peek() != Integer.MIN_VALUE) {