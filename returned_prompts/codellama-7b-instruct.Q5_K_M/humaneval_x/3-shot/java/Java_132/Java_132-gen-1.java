        Stack<Character> stack = new Stack<>();
        for (char c : string.toCharArray()) {
            if (c == '[') {
                stack.push(c);
            } else if (c == ']') {
                if (!stack.isEmpty() && stack.peek() == '[') {
                    stack.pop();
                } else {
                    return true;
                }
            }
        }
        return stack.isEmpty();
    }
}

