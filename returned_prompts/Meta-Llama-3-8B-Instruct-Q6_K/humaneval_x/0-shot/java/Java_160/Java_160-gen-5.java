Here is a simple and efficient solution in Java:

```java
public int doAlgebra(List<String> operator, List<Integer> operand) {
    int result = operand.get(0);
    for (int i = 0; i < operator.size(); i++) {
        String op = operator.get(i);
        int operand1 = operand.get(i);
        int operand2 = operand.get(i + 1);
        switch (op) {
            case "+":
                result += operand2;
                break;
            case "-":
                result -= operand2;
                break;
            case "*":
                result *= operand2;
                break;
            case "/":
                result /= operand2;
                break;
            case "**":
                result = (int) Math.pow(result, operand2);
                break;
        }
    }
    return result;
}
```
In this solution, we start with the first operand as the result. Then we iterate over the operator list and perform the corresponding operation with the next operand. We use a switch statement to handle the different operators. For the "**" operator, we use the Math.pow function to calculate the power. Finally, we return the result. This solution has a time complexity of O(n), where n is the size of the operator list. It is efficient because it only performs the necessary operations to calculate the result.