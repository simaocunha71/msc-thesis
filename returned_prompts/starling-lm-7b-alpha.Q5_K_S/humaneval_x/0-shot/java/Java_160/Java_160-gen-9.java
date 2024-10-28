        int i = 0;
        while (i < operator.size()) {
            if (!operator.get(i).equals("+") && !operator.get(i).equals("-") && !operator.get(i).equals("*") && !operator.get(i).equals("/") && !operator.get(i).equals("**")) {
                break A;
            }
            i++;
        }
        int j = 0;
        while (j < operand.size()) {
            if (!operator.get(i).equals("+") && !operator.get(i).equals("-") && !operator.get(i).equals("*") && !operator.get(i).equals("/") && !operator.get(i).equals("**")) {
                break A;
            }
            j++;
        }
        i += j;
        j = 0;
        while (j < operand.size()) {
            if (j < operand.size() - 1 && !operator.get(i).equals("+") && !operator.get(i).equals("-") && !operator.get(i).equals("*") && !operator.get(i).equals("/") && !operator.get(i).equals("**")) {
                break A;
            }
            j++;
        }
        i += j;
        int result = operand.get(i);
        while (i > 0) {
            int op = operand.get(i - 1);
            int tmp = operand.get(i);
            while (i > 0 && operator.get(i - 1).equals("+")) {
                result += op;
                i--;
                op = operand.get(i);
            }
            while (i > 0 && operator.get(i - 1).equals("-")) {
                result -= op;
                i--;
                op = operand.get(i);
            }
            while (i > 0 && operator.get(i - 1).equals("*")) {
                result *= op;
                i--;
                op = operand.get(i);
            }
            while (i > 0 && operator.