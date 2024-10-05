        String result = "";
        StringBuilder current_string = new StringBuilder();

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (current_string.length() == 0) {
                    current_string.append('_');
                } else if (current_string.length() == 1) {
                    current_string.append('_');
                    result += current_string.toString();
                    current_string.setLength(0);
                } else {
                    current_string.append('-');
                    result += current_string.toString();
                    current_string.setLength(0);
                }
            } else {
                current_string.append(c);
            }
        }
        if (current_string.length() > 0) result += current_string.toString();
        return result;
    }
}

