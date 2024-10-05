        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < brackets.length(); i++) {
            char c = brackets.charAt(i);
            if (c == '<') {
                stack.push(c);
            } else if (c == '>') {
                if (stack.isEmpty()) {
                    return false;
                }
                if (stack.peek() == '<') {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}

This code uses a stack to check if the brackets are correctly nested. It pushes '<' onto the stack and pops it when it finds a '>'. If the stack is empty when it finds a '>', it means there is no matching '<' for this '>', so it returns false. If there is a '<' on the stack when it finds a '>', it means the '<' and '>' are correctly nested, so it pops the '<' from the stack. If the stack is empty at the end, it means all brackets are correctly nested, so it returns true.

The time complexity of this code is O(n), where n is the length of the string, because it processes each character in the string once. The space complexity is O(n) in the worst case when all '<' are followed by '>', because in this case, each '<' could potentially push one character onto the stack.

This code assumes that the input string only contains '<' and '>'. If the input string could contain other characters, you would need to add a check to handle those cases.

I hope this helps. Let me know if you have any other questions.








































































































