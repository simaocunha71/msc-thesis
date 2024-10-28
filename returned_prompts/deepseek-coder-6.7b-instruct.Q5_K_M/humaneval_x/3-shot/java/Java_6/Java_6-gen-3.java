        List<Integer> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                stack.push(0);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    throw new IllegalArgumentException("Unbalanced parentheses");
                }
                int currentLevel = stack.pop() + 1;
                if (!stack.isEmpty()) {
                    int previousLevel = stack.pop();
                    stack.push(Math.max(previousLevel, currentLevel));
                } else {
                    result.add(currentLevel);
                }
            }
        }

        if (!stack.isEmpty()) {
            throw new IllegalArgumentException("Unbalanced parentheses");
        }

        return result;
    }
}

