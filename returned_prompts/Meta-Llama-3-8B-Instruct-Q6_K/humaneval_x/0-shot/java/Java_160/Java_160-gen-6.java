This is a Java solution to the problem. It uses a StringBuilder to construct the algebraic expression and then evaluates it using a calculator.

```java
public int doAlgebra(List<String> operator, List<Integer> operand) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < operand.size() - 1; i++) {
        sb.append(operand.get(i));
        sb.append(operator.get(i));
    }
    sb.append(operand.get(operand.size() - 1));
    return evaluate(sb.toString());
}

public int evaluate(String expression) {
    try {
        return (int) new Object() {
            int evaluate(String expression) {
                return Integer.parseInt(new java.math.BigDecimal(new java.math.BigDecimal(new String(expression)).toString()).intValue());
            }
        }.evaluate(expression);
    } catch (Exception e) {
        return 0;
    }
}
```

This solution assumes that the input lists are valid and follows the rules specified in the problem statement. It also assumes that the output of the evaluation is an integer. If the output is not an integer, it returns 0. You may want to add additional error handling or validation depending on your specific requirements.