```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        // Initialize the result with the first operand
        int result = operand.get(0);

        // Iterate over the operator and operand lists
        for (int i = 0; i < operator.size(); i++) {
            // Get the current operator and the next operand
            String op = operator.get(i);
            int num = operand.get(i + 1);

            // Perform the operation based on the current operator
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

        // Return the final result
        return result;
    }
}
```
