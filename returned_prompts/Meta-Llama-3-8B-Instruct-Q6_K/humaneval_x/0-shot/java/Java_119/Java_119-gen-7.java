    public String matchParens(List<String> lst) {
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
    // Here's the explanation:
    // We iterate over each string in the list.
    // For each string, we iterate over each character.
    // If the character is an open parenthesis, we push it onto the stack.
    // If the character is a close parenthesis, we check if the stack is empty.
    // If the stack is empty, it means there are more close parentheses than open ones, so we return "No".
    // If the stack is not empty, we pop the open parenthesis from the stack.
    // After iterating over all strings, we check if the stack is empty.
    // If it is, it means all parentheses were balanced, so we return "Yes".
    // If the stack is not empty, it means there are more open parentheses than close ones, so we return "No".