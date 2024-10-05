        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String current_op = operator.get(i);
            switch (current_op) {
                case "+":
                    result += operand.get(i + 1);
                    break;
                case "-":
                    result -= operand.get(i + 1);
                    break;
                case "*":
                    result *= operand.get(i + 1);
                    break;
                case "/":
                    result /= operand.get(i + 1);
                    break;
                case "**":
                    result = (int) Math.pow(result, operand.get(i + 1));
                    break;
                default:
                    break;
            }
        }
        return result;
    }
}

