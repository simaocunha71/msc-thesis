        if (operator == null || operand == null) {
            return 0;
        }

        int len = operand.size();
        if (len == 1) {
            return operand.get(0);
        }

        int result = operand.get(0);
        int i = 1;
        while (i < len) {
            if (operator.get(i - 1).equals("+")) {
                result += operand.get(i);
            } else if (operator.get(i - 1).equals("-")) {
                result -= operand.get(i);
            } else if (operator.get(i - 1).equals("*")) {
                result *= operand.get(i);
            } else if (operator.get(i - 1).equals("/")) {
                result /= operand.get(i);
            } else if (operator.get(i - 1).equals("**")) {
                result **= operand.get(i);
            } else {
                // Unknown operator
                return 0;
            }
            i++;
        }
        return result;
    }
}







