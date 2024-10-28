        int open_brackets = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                open_brackets += 1;
            }
            if (c == ']') {
                open_brackets -= 1;
            }
            if (open_brackets < 0) {
                return false;
            }
        }
        return open_brackets > 0;
    }
}

