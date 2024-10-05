        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            int next_operand = operand.get(i + 1);
            if (operator.get(i).equals("+")) {
                result += next_operand;
            } else if (operator.get(i).equals("-")) {
                result -= next_operand;
            } else if (operator.get(i).equals("*")) {
                result *= next_operand;
            } else if (operator.get(i).equals("/")) {
                result /= next_operand;
            } else if (operator.get(i).equals("**")) {
                result = (int) Math.pow(result, next_operand);
            }
        }
        return result;
    }
}

