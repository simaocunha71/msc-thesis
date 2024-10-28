        Stack<Character> stack = new Stack<Character>();

        for (int i = 0; i < brackets.length(); i++) {
            char c = brackets.charAt(i);

            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                if (stack.peek() == '(') {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        }
        return stack.isEmpty();
    }
}

This solution uses a stack to store the brackets. When a '(' is encountered, it is pushed onto the stack. When a ')' is encountered, the top of the stack is checked. If the top of the stack is '(', then it is popped from the stack. If the top of the stack is not '(', then it is pushed onto the stack. If the stack is empty at the end, then every opening bracket has a corresponding closing bracket, and the function returns true. If the stack is not empty, then not every opening bracket has a corresponding closing bracket, and the function returns false.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the string.

Note: This solution assumes that the string only contains '(' and ')'. If the string can contain other characters, then a more complex solution would be needed.

This solution is a good example of how to use a stack data structure to solve a problem related to matching brackets. It is a common problem in computer science and programming interviews.
