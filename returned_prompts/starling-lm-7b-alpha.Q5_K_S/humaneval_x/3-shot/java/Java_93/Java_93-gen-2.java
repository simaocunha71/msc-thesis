        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append((char)((c - 'a' + 1) % 26 + 'a'));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char)((c - 'A' + 1) % 26 + 'A'));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

