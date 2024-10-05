        int open_brackets = 0;
        int close_brackets = 0;

        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                open_brackets += 1;
            } else if (c == '>') {
                close_brackets += 1;

                if (open_brackets < close_brackets) {
                    return false;
                }
            }
        }
        return open_brackets == close_brackets;
    }
}

