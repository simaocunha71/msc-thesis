        List<Integer> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        for(char c : paren_string.toCharArray()) {
            if(c == '(') {
                stack.push(0);
            } else if(c == ')') {
                if(stack.isEmpty()) {
                    continue;
                }
                int current = stack.pop() + 1;
                if(!stack.isEmpty()) {
                    stack.push(Math.max(current, stack.pop()));
                } else {
                    result.add(current);
                }
            }
        }

        return result;
    }
}

