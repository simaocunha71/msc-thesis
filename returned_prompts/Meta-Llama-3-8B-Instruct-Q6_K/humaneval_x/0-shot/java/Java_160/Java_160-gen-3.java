Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        if (operator == null || operand == null) {
            return 0;
        }
        if (operator.size() != operand.size() - 1) {
            return 0;
        }
        if (operator.isEmpty()) {
            return operand.get(0);
        }
        if (operand.size() < 2) {
            return 0;
        }
        int res = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int num = operand.get(i + 1);
            switch (op) {
                case "+":
                    res += num;
                    break;
                case "-":
                    res -= num;
                    break;
                case "*":
                    res *= num;
                    break;
                case "/":
                    res = res / num;
                    break;
                case "**":
                    res = (int) Math.pow(res, num);
                    break;
                default:
                    return 0;
            }
        }
        return res;
    }
}
```

This solution first checks the validity of the input lists. Then, it initializes the result with the first operand. It then iterates over the operator list and applies the corresponding operation to the result and the next operand. Finally, it returns the result. Note that the `/` operator performs integer division, and the `**` operator performs integer exponentiation. If an invalid operator is encountered, the function returns 0.