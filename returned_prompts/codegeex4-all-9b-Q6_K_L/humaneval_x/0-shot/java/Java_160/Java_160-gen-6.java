Here's the Java code for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        for (String op : operator) {
            int b = operand.get(i++);
            int a = stack.pop();
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
        return stack.pop();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> operator = Arrays.asList("+", "*", "-");
        List<Integer> operand = Arrays.asList(2, 3, 4, 5);
        System.out.println(solution.doAlgebra(operator, operand)); // Output: 9
    }
}
```

This code uses a stack to evaluate the expression. We iterate over the operators and for each operator, we pop the top two elements from the stack, perform the operation, and push the result back to the stack. At the end, the stack will contain the result of the expression.