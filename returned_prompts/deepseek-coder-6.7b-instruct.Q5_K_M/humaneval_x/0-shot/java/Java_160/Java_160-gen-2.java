        int result = operand.get(0);
        for (int i = 1; i < operand.size(); i++) {
            switch (operator.get(i - 1)) {
                case "+":
                    result += operand.get(i);
                    break;
                case "-":
                    result -= operand.get(i);
                    break;
                case "*":
                    result *= operand.get(i);
                    break;
                case "/":
                    result /= operand.get(i);
                    break;
                case "**":
                    result = (int)Math.pow(result, operand.get(i));
                    break;
                default:
                    throw new IllegalArgumentException("Invalid operator: " + operator.get(i - 1));
            }
        }
        return result;
    }
}


A: This is a simple implementation of the problem. It uses a for loop to iterate through each element in the operand list starting from the second element (since we already have the first element in the result). Depending on the operator at the corresponding index in the operator list, it performs the corresponding operation on the result and the next operand.

