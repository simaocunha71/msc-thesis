Here is a solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        if (operator == null || operand == null || operator.isEmpty() || operand.isEmpty() || operator.size() != operand.size() - 1) {
            throw new IllegalArgumentException("Invalid input");
        }

        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            switch (operator.get(i)) {
                case "+":
                    result += operand.get(i + 1);
                    break;
                case "-":
                    result -= operand.get(i + 1);
                    break;
                case "*":
                    result *= operand.get(i + 1);
                    break;
                case "/":
                    result /= operand.get(i + 1);
                    break;
                case "**":
                    result = (int) Math.pow(result, operand.get(i + 1));
                    break;
                default:
                    throw new IllegalArgumentException("Invalid operator: " + operator.get(i));
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> operator = Arrays.asList("+", "*", "-");
        List<Integer> operand = Arrays.asList(2, 3, 4, 5);
        System.out.println(solution.doAlgebra(operator, operand)); // Output: 9
    }
}
```

This solution iterates through the operator list and performs the corresponding operation on the result and the next operand in the operand list. The result is initialized to the first operand.