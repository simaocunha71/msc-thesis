        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.push('<');
            } else if (c == '>') {
                if (stack.isEmpty() || stack.pop() != '<') {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}

