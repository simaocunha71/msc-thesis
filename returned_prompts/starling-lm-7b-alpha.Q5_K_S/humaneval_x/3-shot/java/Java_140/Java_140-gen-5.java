        StringBuilder result = new StringBuilder();
        char prev = ' ';
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (prev != ' ') {
                    result.append('_');
                }
                result.append('-');
            } else {
                result.append(c);
            }
            prev = c;
        }
        return result.toString();
    }
}

