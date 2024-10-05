        int result = operand.get(0);

        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int val = operand.get(i + 1);

            if (op.equals("+")) {
                result += val;
            } else if (op.equals("-")) {
                result -= val;
            } else if (op.equals("*")) {
                result *= val;
            } else if (op.equals("/")) {
                result /= val;
            } else if (op.equals("**")) {
                result = (int) Math.pow(result, val);
            }
        }
        return result;
    }
}

