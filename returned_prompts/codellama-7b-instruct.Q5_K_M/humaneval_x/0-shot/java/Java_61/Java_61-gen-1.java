        Stack<Character> stack = new Stack<Character>();
        for (char c : brackets.toCharArray()) {
            switch (c) {
            case '(':
                stack.push(c);
                break;
            case ')':
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
                break;
            }
        }
        return stack.isEmpty();
    }
}

