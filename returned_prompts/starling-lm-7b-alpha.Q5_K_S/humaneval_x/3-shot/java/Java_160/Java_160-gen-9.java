        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < operand.size(); i++) {
            stack.push(operand.get(i));
            if (i == operand.size() - 1) {
                return stack.pop();
            }
            while (true) {
                if (!operator.get(i).equals("+") && !operator.get(i).equals("-")) {
                    stack.push(stack.pop() * stack.pop());
                    continue;
                }
                if (operator.get(i).equals("+")) {
                    int a = stack.pop();
                    int b = stack.pop();
                    stack.push(b + a);
                    continue;
                } else {
                    int a = stack.pop();
                    int b = stack.pop();
                    stack.push(b - a);
                    continue;
                }
                break;
            }
        }
        return stack.pop();
    }
}

