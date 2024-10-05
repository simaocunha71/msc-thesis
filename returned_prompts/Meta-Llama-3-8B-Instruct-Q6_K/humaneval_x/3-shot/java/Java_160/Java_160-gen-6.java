        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            int right_operand = operand.get(i + 1);
            if (operator.get(i).equals("+")) {
                result += right_operand;
            } else if (operator.get(i).equals("-")) {
                result -= right_operand;
            } else if (operator.get(i).equals("*")) {
                result *= right_operand;
            } else if (operator.get(i).equals("/")) {
                result /= right_operand;
            } else if (operator.get(i).equals("**")) {
                result = (int) Math.pow(result, right_operand);
            }
        }
        return result;
    }
}

