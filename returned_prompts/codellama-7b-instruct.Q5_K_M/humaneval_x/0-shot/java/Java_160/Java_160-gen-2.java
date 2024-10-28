        int result = 0;
        int length = operand.size();
        for (int i = 0; i < length - 1; i++) {
            int temp = operand.get(i);
            switch (operator.get(i)) {
                case "+":
                    result += temp;
                    break;
                case "-":
                    result -= temp;
                    break;
                case "*":
                    result *= temp;
                    break;
                case "/":
                    result /= temp;
                    break;
                case "**":
                    result = (int) Math.pow(result, temp);
                    break;
            }
        }
        result += operand.get(length - 1);
        return result;
    }
}

