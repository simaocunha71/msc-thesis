        int result = operand.get(0);
        for (int i = 1; i < operand.size(); i++) {
            switch (operator.get(i-1)) {
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
                    result = (int)Math.pow(result,operand.get(i));
                    break;
            }
        }
        return result;
    }
}

