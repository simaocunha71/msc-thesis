    public String encrypt(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                sb.append((char) ((c - base + 8 * 2) % 26 + base));
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
