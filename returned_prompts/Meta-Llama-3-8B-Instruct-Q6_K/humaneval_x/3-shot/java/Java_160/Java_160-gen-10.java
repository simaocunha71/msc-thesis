        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int b = operand.get(i + 1);
            switch (op) {
                case "+":
                    result += b;
                    break;
                case "-":
                    result -= b;
                    break;
                case "*":
                    result *= b;
                    break;
                case "/":
                    result /= b;
                    break;
                case "**":
                    result = (int) Math.pow(result, b);
                    break;
            }
        }
        return result;
    }
}

