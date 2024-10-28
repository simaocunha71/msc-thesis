```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int num = operand.get(i + 1);
            if (op.equals("+")) {
                result += num;
            } else if (op.equals("-")) {
                result -= num;
            } else if (op.equals("*")) {
                result *= num;
            } else if (op.equals("/")) {
                result /= num;
            } else if (op.equals("**")) {
                result = (int) Math.pow(result, num);
            }
        }
        return result;
    }
}
```