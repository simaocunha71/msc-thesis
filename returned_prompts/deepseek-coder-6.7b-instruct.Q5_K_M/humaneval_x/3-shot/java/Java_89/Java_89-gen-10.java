        StringBuilder encrypted = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                encrypted.append((char) ('E' + (c - 'A' + 2) % 26));
            } else {
                encrypted.append((char) ('e' + (c - 'a' + 2) % 26));
            }
        }

        return encrypted.toString();
    }
}

