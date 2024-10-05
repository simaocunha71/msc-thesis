        int result = operand.get(0);
        for (int i = 0; i < operator.size(); i++) {
            int operand1 = operand.get(i);
            int operand2 = operand.get(i + 1);
            if (operator.get(i).equals("+")) {
                result += operand2;
            } else if (operator.get(i).equals("-")) {
                result -= operand2;
            } else if (operator.get(i).equals("*")) {
                result *= operand2;
            } else if (operator.get(i).equals("/")) {
                result /= operand2;
            } else if (operator.get(i).equals("**")) {
                result = (int) Math.pow(result, operand2);
            }
        }
        return result;
    }
}

