        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            if (operator.get(i).equals("+")) {
                result += operand.get(i + 1);
            } else if (operator.get(i).equals("-")) {
                result -= operand.get(i + 1);
            } else if (operator.get(i).equals("*")) {
                result *= operand.get(i + 1);
            } else if (operator.get(i).equals("/")) {
                result /= operand.get(i + 1);
            } else if (operator.get(i).equals("**")) {
                result = (int) Math.pow(result, operand.get(i + 1));
            }
        }
        return result;
    }
}

