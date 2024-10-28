        int result = operand.get(0);
        for (int i = 1; i < operand.size(); i++) {
            if (operator.get(i - 1).equals("+")) {
                result += operand.get(i);
            } else if (operator.get(i - 1).equals("-")) {
                result -= operand.get(i);
            } else if (operator.get(i - 1).equals("*")) {
                result *= operand.get(i);
            } else if (operator.get(i - 1).equals("/")) {
                result /= operand.get(i);
            } else if (operator.get(i - 1).equals("**")) {
                result = (int) Math.pow(result, operand.get(i));
            }
        }
        return result;
    }
}

