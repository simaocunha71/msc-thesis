    Stack<Character> stack = new Stack<Character>();

    for (String s : lst) {
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    return "No";
                } else {
                    stack.pop();
                }
            }
        }
    }

    if (stack.isEmpty()) {
        return "Yes";
    } else {
        return "No";
    }
}
}

Here the stack is used to store the opening parentheses and whenever a closing parenthesis is encountered, it is compared to the latest opening parenthesis in the stack. If the stack is empty, that means there is no matching opening parenthesis for the closing one, so "No" is returned. If at the end of the iteration the stack is empty, that means all parentheses were matched, so "Yes" is returned.

The time complexity is O(n