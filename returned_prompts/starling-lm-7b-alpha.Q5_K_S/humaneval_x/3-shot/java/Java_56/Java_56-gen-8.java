        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.add(c);
            } else if (c == '>') {
                if (stack.isEmpty()) return false;
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}

