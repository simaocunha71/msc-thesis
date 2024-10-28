```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        for (int op : operand) {
            if (i < operator.size()) {
                String s = operator.get(i);
                if (s.equals("+")) {
                    stack.push(op);
                } else if (s.equals("-")) {
                    stack.push(-op);
                } else if (s.equals("*")) {
                    stack.push(stack.pop() * op);
                } else if (s.equals("/")) {
                    stack.push(stack.pop() / op);
                } else if (s.equals("**")) {
                    stack.push((int) Math.pow(stack.pop(), op));
                }
                i++;
            } else {
                stack.push(op);
            }
        }
        int result = 0;
        while (!stack.isEmpty()) {
            result += stack.pop();
        }
        return result;
    }
}
```

Explanation:
The algorithm uses a stack to store the operands. It iterates through the operator list and performs the corresponding operation on the operands in the stack. Finally, it sums up the elements in the stack and returns the result. The time complexity is O(n), where n is the length of the operand list.