        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            String op = operator.get(i);
            int left = operand.get(i);
            int right = operand.get(i + 1);
            if (op.equals("+")) {
                result += right;
            } else if (op.equals("-")) {
                result -= right;
            } else if (op.equals("*")) {
                result *= right;
            } else if (op.equals("/")) {
                result /= right;
            } else {
                result = (int) Math.pow(result, right);
            }
        }
        return result;
    }
}

