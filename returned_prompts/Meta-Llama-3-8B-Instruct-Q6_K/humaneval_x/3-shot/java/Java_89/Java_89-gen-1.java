        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                result.append((char) ((c - base + 8) % 26 + base));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

