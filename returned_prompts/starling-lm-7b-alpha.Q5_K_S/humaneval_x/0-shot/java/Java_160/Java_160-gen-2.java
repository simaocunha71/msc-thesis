        int result = 0;
        Stack<Integer> stack = new Stack<>();
        Stack<String> operators = new Stack<>();
        for (int i = 0; i < operator.size(); i++) {
            if (operator.get(i).equals("+")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b + a);
            } else if (operator.get(i).equals("-")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b - a);
            } else if (operator.get(i).equals("*")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b * a);
            } else if (operator.get(i).equals("/")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b / a);
            } else {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b * a);
                operators.push(operator.get(i));
            }
        }
        result = stack.pop();
        while (!operators.isEmpty()) {
            if (operators.pop().equals("*")) {
                result *= stack.pop();
                stack.push(result);
            } else {
                stack.push(result);
                result = stack.pop();
                while (!operators.isEmpty() && operators.pop().equals("*")) {
                    int a = stack.pop();
                    int b = stack.pop();
                    stack.push(b * a);
                }
                result *= stack.pop();
                stack.push(result);
            }
        }
        return result;
    }
}


























































