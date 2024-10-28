```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        // Initialize a stack to store operands
        Stack<Integer> stack = new Stack<>();

        // Iterate through the operator and operand lists
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int num = operand.get(i);

            // Perform the operation based on the current operator
            switch (op) {
                case "+":
                    // Push the result of the addition to the stack
                    stack.push(stack.pop() + num);
                    break;
                case "-":
                    // Push the result of the subtraction to the stack
                    stack.push(stack.pop() - num);
                    break;
                case "*":
                    // Push the result of the multiplication to the stack
                    stack.push(stack.pop() * num);
                    break;
                case "/":
                    // Push the result of the floor division to the stack
                    stack.push(stack.pop() / num);
                    break;
                case "**":
                    // Push the result of the exponentiation to the stack
                    stack.push((int) Math.pow(stack.pop(), num));
                    break;
            }
        }

        // The final result will be the only element left in the stack
        return stack.pop();
    }
}
```
