        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < brackets.length(); i++) {
            char c = brackets.charAt(i);
            if (c == '(') {
                stack.add(c);
            } else if (c == ')') {
                if (stack.size() == 0) return false;
                stack.pop();
            }
        }
        return stack.size() == 0;
    }
}

