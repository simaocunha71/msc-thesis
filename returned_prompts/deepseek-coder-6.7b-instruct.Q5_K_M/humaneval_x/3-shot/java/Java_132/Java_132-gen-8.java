        Stack<Character> stack = new Stack<>();

        for (char c : string.toCharArray()) {
            if (c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                if (stack.peek() == '[') {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }

        return !stack.isEmpty();
     }
}

