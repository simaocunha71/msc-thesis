        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.push(c);
            } else if (c == '>' && stack.isEmpty()) {
                return false;
            } else if (c == '>') {
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}


