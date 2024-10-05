        StringBuilder result = new StringBuilder();
        boolean prev_was_space = false;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (prev_was_space) {
                    result.append('-');
                } else {
                    result.append('_');
                }
                prev_was_space = true;
            } else {
                result.append(c);
                prev_was_space = false;
            }
        }
        return result.toString();
    }
}

