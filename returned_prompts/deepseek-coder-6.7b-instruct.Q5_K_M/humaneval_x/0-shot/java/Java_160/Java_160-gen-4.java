
The given program is not correct because it is not considering the precedence of operations (BODMAS rule). In your example, it should give 11 (2 + 3 * 4 - 5), but the current program gives 9 (2 + 3 * 4), because it is not considering the subtraction operation.

So, the correct program should be:

```java
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
```

This program evaluates the expression by following the BODM