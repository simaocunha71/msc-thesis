Here is the Java code that implements the problem:

```java
import java.util.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int operand1 = operand.get(i);
            int operand2 = operand.get(i + 1);
            if (op.equals("+")) {
                result += operand2;
            } else if (op.equals("-")) {
                result -= operand2;
            } else if (op.equals("*")) {
                result *= operand2;
            } else if (op.equals("/")) {
                result /= operand2;
            } else if (op.equals("**")) {
                result = (int) Math.pow(result, operand2);
            }
        }
        return result;
    }
}
```
In this code, we iterate through the operator list and the operand list simultaneously. We use a variable `result` to store the intermediate result of the expression. For each operator, we perform the corresponding operation on the `result` and the next operand. Finally, we return the `result` as the final evaluation of the expression. 

Note that we handle the division operation by integer division (`/`), which discards the remainder. If you want to perform floating-point division, you can use the `double` type and the `/` operator. 

Also, note that we use `Math.pow` for exponentiation, which returns a `double` value. If you want to perform integer exponentiation, you can use the `Math.pow` method with an integer argument and then cast the result to an `int`. 

The time complexity of this solution is O(n), where n is the length of the operator list, since we iterate through the list once. The space complexity is O(1), since we only use a constant amount of space to store the `result` variable. 