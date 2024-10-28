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
}

