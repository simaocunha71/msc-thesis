        int open_count = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                open_count += 1;
            } else if (c == ')') {
                if (open_count == 0) {
                    return false;
                }
                open_count -= 1;
            }
        }
        return open_count == 0;
    }
}

