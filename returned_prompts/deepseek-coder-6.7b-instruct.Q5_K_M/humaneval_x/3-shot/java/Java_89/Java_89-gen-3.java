        StringBuilder encrypted = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                encrypted.append((char) ('A' + (c - 'A' + 10) % 26));
            } else {
                encrypted.append((char) ('a' + (c - 'a' + 10) % 26));
            }
        }
        return encrypted.toString();
    }
}

