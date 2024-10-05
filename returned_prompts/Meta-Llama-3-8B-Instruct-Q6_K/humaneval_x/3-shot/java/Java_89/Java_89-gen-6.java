        StringBuilder encrypted = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                c = (char) ((c - 'a' + 2 * 2) % 26 + 'a');
            } else if (c >= 'A' && c <= 'Z') {
                c = (char) ((c - 'A' + 2 * 2) % 26 + 'A');
            }
            encrypted.append(c);
        }
        return encrypted.toString();
    }
}

