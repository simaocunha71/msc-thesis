        int current_depth = 0;
        int max_depth = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                current_depth += 1;
                max_depth = Math.max(max_depth, current_depth);
            } else if (c == ']') {
                current_depth -= 1;
            }
        }
        return max_depth > 0;
    }
}

