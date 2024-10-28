        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            int a = operand.get(i);
            int b = operand.get(i + 1);
            if (operator.get(i).equals("+")) {
                result += b;
            } else if (operator.get(i).equals("-")) {
                result -= b;
            } else if (operator.get(i).equals("*")) {
                result *= b;
            } else if (operator.get(i).equals("/")) {
                result /= b;
            } else if (operator.get(i).equals("**")) {
                result = (int) Math.pow(result, b);
            }
        }
        return result;
    }
}

