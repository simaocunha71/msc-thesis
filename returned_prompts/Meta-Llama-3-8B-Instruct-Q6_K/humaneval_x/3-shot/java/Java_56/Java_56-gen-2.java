        int open = 0;
        int close = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                open++;
            } else if (c == '>') {
                close++;
                if (open < close) {
                    return false;
                }
            }
        }
        return open == close;
    }
}

