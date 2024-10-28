        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.add(c);
            } else if (c == '>') {
                if (stack.size() == 0) return false;
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.size() == 0;
    }
}

