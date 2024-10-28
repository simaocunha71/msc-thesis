        Stack<Integer> stack = new Stack<>();
        Stack<String> stack_operator = new Stack<>();

        for (int i = 0; i < operator.size(); i++) {
            if (operator.get(i).equals("+")) {
                stack.push(stack.pop() + operand.get(i));
            } else if (operator.get(i).equals("-")) {
                stack.push(stack.pop() - operand.get(i));
            } else if (operator.get(i).equals("*")) {
                stack.push(stack.pop() * operand.get(i));
            } else if (operator.get(i).equals("/")) {
                stack.push(stack.pop() / operand.get(i));
            } else if (operator.get(i).equals("**")) {
                stack.push((int) Math.pow(stack.pop(), operand.get(i)));
            }
        }
        return stack.pop();
    }
}

