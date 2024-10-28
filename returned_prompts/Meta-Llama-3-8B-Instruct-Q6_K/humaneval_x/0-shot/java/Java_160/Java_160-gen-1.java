```java
import java.util.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int num = operand.get(i + 1);
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
        return result;
    }
}
```


Explanation:
The given problem is to build an algebraic expression using the given list of operators and operands. The expression is then evaluated and the result is returned.

The approach used is to iterate through the operator list and for each operator, perform the corresponding operation on the current result and the next operand in the operand list. The result is updated after each operation.

In the given code, we start with the first operand as the initial result. Then, for each operator, we perform the corresponding operation on the current result and the next operand. The result is updated after each operation. Finally, the updated result is returned.

The switch statement is used to handle the different operators and perform the corresponding operations. The Math.pow function is used to handle the exponentiation operation.

Note that the operator list has at least one operator, and the operand list has at least two operands. The length of the operator list is equal to the length of the operand list minus one. The operands are non-negative integers.