```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
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
            }
        }
        return result;
    }
}
```