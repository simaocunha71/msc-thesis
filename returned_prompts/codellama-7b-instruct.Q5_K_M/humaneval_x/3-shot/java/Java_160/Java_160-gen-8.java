        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            int right = operand.get(i + 1);
            switch (operator.get(i)) {
                case "+":
                    result += right;
                    break;
                case "-":
                    result -= right;
                    break;
                case "*":
                    result *= right;
                    break;
                case "/":
                    result /= right;
                    break;
                case "**":
                    result = (int) Math.pow(result, right);
                    break;
                default:
                    break;
            }
        }
        return result;
    }
}

