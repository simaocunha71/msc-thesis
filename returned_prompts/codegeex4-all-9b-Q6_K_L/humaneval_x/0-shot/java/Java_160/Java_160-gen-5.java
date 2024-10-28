```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        Deque<Integer> stack = new ArrayDeque<>();
        int i = 0;
        for (String op : operator) {
            int a = stack.pop();
            int b = operand.get(i++);
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
                    stack.push((int)Math.pow(a, b));
                    break;
            }
        }
        return stack.pop();
    }
}
```