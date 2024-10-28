        int depth = 0;
        boolean seen_open = false;
        boolean seen_close = false;

        for (char c : string.toCharArray()) {
            if (c == '[') {
                seen_open = true;
                depth += 1;
            } else if (c == ']') {
                seen_close = true;
                depth -= 1;
            }

            if (seen_open && seen_close && depth == 0) {
                return true;
            }
        }
        return false;
    }
}

