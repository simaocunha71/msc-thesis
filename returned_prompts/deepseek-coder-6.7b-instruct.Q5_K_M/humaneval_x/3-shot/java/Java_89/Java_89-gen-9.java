        StringBuilder encrypted = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                encrypted.append((char) ('A' + (c - 'A' + 2) % 26 * 2));
            } else {
                encrypted.append((char) ('a' + (c - 'a' + 2) % 26 * 2));
            }
        }
        return encrypted.toString();
    }
}

