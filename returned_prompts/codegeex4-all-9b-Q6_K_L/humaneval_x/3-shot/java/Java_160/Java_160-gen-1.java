        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < operand.size(); i++) {
            if (i == operand.size() - 1) {
                stack.push(operand.get(i));
            } else if (operator.get(i).equals("+")) {
                stack.push(operand.get(i) + operand.get(i + 1));
            } else if (operator.get(i).equals("-")) {
                stack.push(operand.get(i) - operand.get(i + 1));
            } else if (operator.get(i).equals("*")) {
                stack.push(operand.get(i) * operand.get(i + 1));
            } else {
                stack.push(operand.get(i) / operand.get(i + 1));
            }
        }
        return stack.pop();
    }
}

