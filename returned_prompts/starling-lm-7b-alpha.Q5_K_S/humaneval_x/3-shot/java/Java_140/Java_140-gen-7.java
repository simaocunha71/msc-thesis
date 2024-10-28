        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == ' ') {
                result.append("_");
            } else {
                result.append(c);
            }
            if (i + 1 < text.length() && text.charAt(i + 1) == ' ') {
                i += 1;
                result.append('-');
            }
        }
        return result.toString();
    }
}

