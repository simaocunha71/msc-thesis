        Stack<Character> stack = new Stack<>();
        for (char c : string.toCharArray()) {
            if (c == '[') {
                stack.push(c);
            } else if (c == ']') {
                if (stack.empty()) {
                    return false;
                }
                stack.pop();
            }
        }
        if (stack.empty()) {
            return true;
        }
        return false;
    }
}

