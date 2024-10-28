        Stack<Character> stack = new Stack<>();
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    stack.push(c);
                } else {
                    if (stack.isEmpty()) {
                        return "No";
                    }
                    stack.pop();
                }
            }
        }
        return stack.isEmpty() ? "Yes" : "No";
    }
}

