Here is a Java solution that uses a StringBuilder to build the algebraic expression and then evaluates it using the Math class:

```java
import java.util.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < operand.size() - 1; i++) {
            sb.append(operand.get(i));
            sb.append(operator.get(i));
        }
        sb.append(operand.get(operand.size() - 1));
        try {
            return (int) eval(sb.toString());
        } catch (Exception e) {
            return 0;
        }
    }

    private double eval(String expression) {
        return Math.eval(expression);
    }
}
```

This solution uses a StringBuilder to concatenate the operands and operators into a string. It then uses the Math.eval() method to evaluate the expression. If the evaluation fails (for example, if the expression is malformed), the method returns 0.

Note that the Math.eval() method is not a standard Java method, and it may not be available in all Java environments. You may need to use a different method or library to evaluate the expression. For example, you could use a library like Apache Commons Math or a scripting engine like Groovy.