        StringBuilder result = new StringBuilder();
        int consecutive_spaces = 0;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (consecutive_spaces == 0) {
                    result.append(c);
                    consecutive_spaces += 1;
                } else {
                    result.append('-');
                    consecutive_spaces += 1;
                }
            } else {
                result.append(c);
                consecutive_spaces = 0;
            }
        }
        return result.toString();
    }
}

