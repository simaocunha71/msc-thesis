        Stack<Character> stack = new Stack<>();

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

// This solution uses a stack to keep track of the brackets. If it finds an opening bracket, it pushes it onto the stack. If it finds a closing bracket, it checks the top of the stack. If the top of the stack is an opening bracket, it pops it off the stack. If the top of the stack is not an opening bracket, it pushes the closing bracket onto the stack. If the stack is empty at the end, it means all brackets were correctly matched and returns true. If the stack is not empty at the end, it means there were unmatched opening brackets and returns false.

// The time complexity of this solution is O(n) where n is the length of the string. This is because it goes through the string once.
// The space complexity is also O(n) in the worst case scenario where all brackets are opening brackets. In this case, we would need to store all of them in the stack.

// This solution assumes that the input string only contains '(' and ')' characters. If the input could contain other characters, the solution would need to be modified accordingly.

// This solution assumes that the input string is not null. If the input could be null, the solution would need to be modified to handle this case.

// This solution assumes that the input string is well-formed. If the input could be malformed (e.g., there could be extra closing brackets without a corresponding opening bracket), the solution would need to be modified to handle this case.

// This solution assumes that the input string is ASCII. If the input could be Unicode, the solution would need to be modified to handle