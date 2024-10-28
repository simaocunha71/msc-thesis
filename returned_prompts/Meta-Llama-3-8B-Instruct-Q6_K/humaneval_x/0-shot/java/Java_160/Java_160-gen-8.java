Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        if (operator == null || operand == null) {
            return 0;
        }
        if (operator.size() == 0 || operand.size() < 2) {
            return 0;
        }
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < operand.size(); i++) {
            stack.push(operand.get(i));
            if (i < operator.size()) {
                int b = stack.pop();
                int a = stack.pop();
                String op = operator.get(operator.size() - 1 - i);
                switch (op) {
                    case "+":
                        stack.push(a + b);
                        break;
                    case "-":
                        stack.push(a - b);
                        break;
                    case "*":
                        stack.push(a * b);
                        break;
                    case "/":
                        stack.push(a / b);
                        break;
                    case "**":
                        stack.push((int) Math.pow(a, b));
                        break;
                }
            }
        }
        return stack.pop();
    }
}
```

The algorithm is based on a stack. For each operator, we pop the top two operands from the stack, apply the operation, and push the result back to the stack. Finally, the result of the algebra expression is the only element left in the stack. If the operator list is empty, we return 0. If the operand list has less than two elements, we also return 0. If the input lists are null, we return 0. Otherwise, we start the stack and the loop to process the operators and operands. The time complexity is O(n), where n is the size of the operand list. The space complexity is also O(n), as we use a stack to store the intermediate results.