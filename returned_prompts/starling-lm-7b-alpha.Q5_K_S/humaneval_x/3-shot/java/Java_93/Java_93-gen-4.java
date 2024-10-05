        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    result.append((char)(((c - 'a') + 2) % 26 + 'a'));
                } else {
                    result.append((char)(((c - 'a') + 26 - 1) % 26 + 'a'));
                }
            } else if (c >= 'A' && c <= 'Z') {
                if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                    result.append((char)(((c - 'A') + 2) % 26 + 'A'));
                } else {
                    result.append((char)(((c - 'A') + 26 - 1) % 26 + 'A'));
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

