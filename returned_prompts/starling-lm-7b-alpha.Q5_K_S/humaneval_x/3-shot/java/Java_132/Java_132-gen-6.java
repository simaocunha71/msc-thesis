        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == '[') {
                stack.push('[');
            } else {
                if (stack.size() == 0) return false;
                stack.pop();
            }
        }
        return stack.size() == 0;
    }
}

