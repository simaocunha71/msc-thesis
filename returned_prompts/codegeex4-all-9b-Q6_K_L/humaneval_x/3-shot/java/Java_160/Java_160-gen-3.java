        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String current_operator = operator.get(i);
            if (current_operator.equals("+")) {
                result += operand.get(i + 1);
            } else if (current_operator.equals("-")) {
                result -= operand.get(i + 1);
            } else if (current_operator.equals("*")) {
                result *= operand.get(i + 1);
            } else if (current_operator.equals("/")) {
                result /= operand.get(i + 1);
            } else if (current_operator.equals("**")) {
                result = (int) Math.pow(result, operand.get(i + 1));
            }
        }
        return result;
    }
}

