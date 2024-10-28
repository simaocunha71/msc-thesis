        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < operator.size(); i++) {
            String operator_i = operator.get(i);
            if (operator_i.equals("+")) {
                stack.push(stack.pop() + operand.get(i));
            } else if (operator_i.equals("-")) {
                stack.push(-stack.pop() + operand.get(i));
            } else if (operator_i.equals("*")) {
                stack.push(stack.pop() * operand.get(i));
            } else if (operator_i.equals("/")) {
                stack.push(stack.pop() / operand.get(i));
            } else {
                stack.push(stack.pop() ** operand.get(i));
            }
        }
        return stack.pop();
    }
}

