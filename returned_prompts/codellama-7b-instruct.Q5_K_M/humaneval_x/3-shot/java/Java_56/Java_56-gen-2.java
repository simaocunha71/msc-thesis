        int open_brackets = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                open_brackets += 1;
            } else if (c == '>') {
                open_brackets -= 1;
            }
        }
        return open_brackets == 0;
    }
}

