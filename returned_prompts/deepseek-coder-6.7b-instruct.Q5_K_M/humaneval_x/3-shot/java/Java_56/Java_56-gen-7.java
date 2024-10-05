        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
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

