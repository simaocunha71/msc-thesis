Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        if (operator == null || operand == null || operator.size() != operand.size() - 1) {
            throw new RuntimeException("Invalid input");
        }

        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            int operand1 = operand.get(i);
            int operand2 = operand.get(i + 1);
            switch (operator.get(i)) {
                case "+":
                    result += operand2;
                    break;
                case "-":
                    result -= operand2;
                    break;
                case "*":
                    result *= operand2;
                    break;
                case "/":
                    result /= operand2;
                    break;
                case "**":
                    result = (int) Math.pow(result, operand2);
                    break;
                default:
                    throw new RuntimeException("Invalid operator");
            }
        }
        return result;
    }
}
```

This solution works by iterating over the operator list and operand list simultaneously. It uses a switch statement to determine the operation to perform based on the operator. The result is updated accordingly. If the operator is not one of the basic algebra operations, a RuntimeException is thrown. The solution also checks for invalid input at the beginning.