        int open_bracket_count = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                open_bracket_count += 1;
            } else if (c == ']') {
                open_bracket_count -= 1;
            }

            if (open_bracket_count < 0) {
                return true;
            }
        }
        return open_bracket_count == 0;
    }
}

