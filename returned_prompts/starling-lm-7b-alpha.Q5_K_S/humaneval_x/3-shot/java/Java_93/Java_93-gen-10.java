        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c == ' ') {
                result.append(' ');
            } else if (c >= 'a' && c <= 'z') {
                result.append((char) (c - 'a' + 'A'));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char) (c + 'z' - 'A'));
            } else if (c >= 'a' && c <= 'z') {
                result.append((char) (c - 'a' + 26 + 'A'));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char) (c + 'a' - 'A'));
            }
        }
        return result.toString();
    }
}

