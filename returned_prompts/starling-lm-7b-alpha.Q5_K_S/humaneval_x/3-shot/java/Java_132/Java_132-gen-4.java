        int current_depth = 0;

        for (char c : string.toCharArray()) {
            if (c == '[') {
                current_depth += 1;
            } else if (c == ']') {
                current_depth -= 1;
            }

            if (current_depth < 0) {
                return true;
            }
        }
        return false;
    }
}

