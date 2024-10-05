        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                result.append((char)((c - 'a' + 2 * 2) % 26 + 'a'));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char)((c - 'A' + 2 * 2) % 26 + 'A'));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

