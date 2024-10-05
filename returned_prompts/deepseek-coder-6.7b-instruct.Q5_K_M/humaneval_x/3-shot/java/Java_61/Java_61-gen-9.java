        Stack<Character> stack = new Stack<>();

        for (char bracket : brackets.toCharArray()) {
            if (bracket == '(') {
                stack.push(bracket);
            } else if (stack.isEmpty()) {
                return false;
            } else {
                stack.pop();
            }
        }

        return stack.isEmpty();
     }
}

