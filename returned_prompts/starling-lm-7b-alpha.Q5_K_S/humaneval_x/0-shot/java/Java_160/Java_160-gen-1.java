        int n = operator.size();
        int m = operand.size();
        int result = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        Deque<String> stack1 = new ArrayDeque<>();
        for (int i = 0; i < n + m; i++) {
            if (operator.get(i).equals("+")) {
                result += stack.pop();
                stack1.pop();
            } else if (operator.get(i).equals("-")) {
                result -= stack.pop();
                stack1.pop();
            } else if (operator.get(i).equals("*")) {
                result *= stack.pop();
                stack1.pop();
            } else if (operator.get(i).equals("/")) {
                result /= stack.pop();
                stack1.pop();
            } else if (operator.get(i).equals("**")) {
                result = (int) Math.pow(stack.pop(), stack.pop());
                stack1.pop();
            } else {
                stack.push(operand.get(i));
                stack1.push(operator.get(i));
            }
        }
        return result;
    }
}















































































































































































































