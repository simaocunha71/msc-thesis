        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < brackets.length(); i++) {
            char c = brackets.charAt(i);
            if (c == '<') {
                stack.push(c);
            } else if (!stack.isEmpty() && stack.peek() == '<') {
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.isEmpty();
    }
}

