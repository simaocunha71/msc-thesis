        /**
        A solution I found online:
        https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
         */
        Stack<Character> stack = new Stack<Character>();
        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.empty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.empty();
    }
}
