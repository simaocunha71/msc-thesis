```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        // Initialize the result with the first operand
        int result = operand.get(0);
        
        // Iterate over the operator list
        for (int i = 0; i < operator.size(); i++) {
            // Get the current operator
            String op = operator.get(i);
            
            // Get the current operand
            int num = operand.get(i + 1);
            
            // Perform the operation
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
            }
        }
        
        // Return the result
        return result;
    }
}
```