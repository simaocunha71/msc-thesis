        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append((char)('a' + (((c - 'a') + 4) % 26)));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char)('A' + (((c - 'A') + 4) % 26)));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

