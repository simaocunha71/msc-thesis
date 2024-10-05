        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == ' ') {
                result.append("_");
            } else if (i + 1 < text.length()) {
                char next = text.charAt(i + 1);
                if (next == ' ') {
                    result.append("-");
                    i += 1;
                } else {
                    result.append(c);
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

