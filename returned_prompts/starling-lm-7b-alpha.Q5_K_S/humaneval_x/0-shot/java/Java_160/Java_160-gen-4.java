        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < operator.size(); i++) {
            String s = operator.get(i);
            if (s.equals("+")) {
                stack.push(operand.get(i));
                stack.push(operand.get(i + 1));
            } else if (s.equals("-")) {
                stack.push(operand.get(i));
                stack.push(-operand.get(i + 1));
                i++;
            } else if (s.equals("*")) {
                int a = operand.get(i);
                int b = operand.get(i + 1);
                stack.push(a * b);
                i++;
            } else if (s.equals("/")) {
                int a = operand.get(i);
                int b = operand.get(i + 1);
                stack.push(a / b);
                i++;
            } else {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a ^ b);
            }
        }
        return stack.pop();
    }
}
























































































































































































































