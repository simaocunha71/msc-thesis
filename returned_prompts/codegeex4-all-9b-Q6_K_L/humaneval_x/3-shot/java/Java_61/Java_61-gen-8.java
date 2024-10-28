        int current_depth = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
            } else if (c == ')') {
                current_depth -= 1;
                if (current_depth < 0) {
                    return false;
                }
            }
        }
        return current_depth == 0;
    }
}

