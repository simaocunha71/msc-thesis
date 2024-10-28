        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                if (c == base || c == base + 1 || c == base + 2 || c == base + 3 || c == base + 4 || c == base + 5 || c == base + 6) {
                    result.append((char) (base + 6));
                } else {
                    result.append((char) (base + (c - base + 2) % 26));
                }
            } else {
                result.append(c);
            }
        }
        return result.toString().toLowerCase();
    }
}

