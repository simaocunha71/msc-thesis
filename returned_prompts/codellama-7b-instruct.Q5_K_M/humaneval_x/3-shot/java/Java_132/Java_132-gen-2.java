        int open_bracket_count = 0;
        int close_bracket_count = 0;

        for (char c : string.toCharArray()) {
            if (c == '[') {
                open_bracket_count += 1;
            } else if (c == ']') {
                close_bracket_count += 1;
            }
        }

        return open_bracket_count > close_bracket_count;
    }
}

