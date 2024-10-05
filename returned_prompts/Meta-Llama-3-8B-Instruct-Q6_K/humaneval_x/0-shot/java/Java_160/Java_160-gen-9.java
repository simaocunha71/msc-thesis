The problem is asking to evaluate a mathematical expression constructed from the given operator and operand lists. The operator list contains basic algebra operations, and the operand list contains integers. The expression is built by combining the operators with the corresponding operands.

Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        int result = operand.get(0);
        for(int i = 0; i < operator.size(); i++){
            String op = operator.get(i);
            int num = operand.get(i + 1);
            switch(op){
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
                    result = (int)Math.pow(result, num);
                    break;
            }
        }
        return result;
    }
}
```

The solution uses a for loop to iterate over the operator list. For each operator, it gets the corresponding operand from the operand list and applies the operation to the result. The result is updated accordingly. Finally, the solution returns the final result.

For example, if the operator list is ["+", "*", "-"] and the operand list is [2, 3, 4, 5], the solution will evaluate the expression as follows:

2 + 3 = 5
5 * 4 = 20
20 - 5 = 15

The final result is 15.