        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();
    }
}

