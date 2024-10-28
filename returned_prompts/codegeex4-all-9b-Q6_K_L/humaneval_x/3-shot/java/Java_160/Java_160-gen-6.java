        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < operator.size(); i++) {
            int operand1 = stack.pop();
            int operand2 = operand.get(i);
            int result = 0;

            if (operator.get(i).equals("+")) {
                result = operand1 + operand2;
            } else if (operator.get(i).equals("-")) {
                result = operand1 - operand2;
            } else if (operator.get(i).equals("*")) {
                result = operand1 * operand2;
            } else if (operator.get(i).equals("/")) {
                result = operand1 / operand2;
            } else if (operator.get(i).equals("**")) {
                result = (int) Math.pow(operand1, operand2);
            }
            stack.push(result);
        }
        return stack.pop();
    }
}

