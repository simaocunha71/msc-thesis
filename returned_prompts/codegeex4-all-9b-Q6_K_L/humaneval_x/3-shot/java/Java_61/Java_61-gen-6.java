        int open = 0;
        int close = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                open += 1;
            } else if (c == ')') {
                close += 1;
            }
        }

        return open == close;
    }
}

