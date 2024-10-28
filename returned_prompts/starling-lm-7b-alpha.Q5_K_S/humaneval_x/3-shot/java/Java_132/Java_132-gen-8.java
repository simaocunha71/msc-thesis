        int left_depth = 0;
        int right_depth = 0;

        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (c == '[') {
                left_depth += 1;
            } else if (c == ']') {
                right_depth += 1;
            }
            if (left_depth < right_depth) return true;
        }
        return left_depth > 0;

    }
}

