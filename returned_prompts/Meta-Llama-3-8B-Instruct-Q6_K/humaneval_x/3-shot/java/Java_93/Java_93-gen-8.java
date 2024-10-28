        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                if (c == base) {
                    result.append(base);
                } else if (c == base + 1 || c == base + 2) {
                    result.append((char) ((c + 1) % 26 + base));
                } else {
                    result.append((char) ((c - 2) % 26 + base));
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}