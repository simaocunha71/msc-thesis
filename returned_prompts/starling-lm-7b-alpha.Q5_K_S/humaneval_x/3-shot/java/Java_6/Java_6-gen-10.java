        List<Integer> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        int current_depth = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                stack.push(current_depth);
                current_depth += 1;
            } else if (c == ')') {
                current_depth -= 1;
                result.add(current_depth);
                if (stack.size() > 0) {
                    current_depth = stack.pop();
                }
            }
        }
        return result;
    }
}

