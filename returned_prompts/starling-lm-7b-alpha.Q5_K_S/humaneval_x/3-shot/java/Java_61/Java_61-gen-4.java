        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.size() == 0) return false;
                stack.pop();
            }
        }
        return stack.size() == 0;
    }
}

