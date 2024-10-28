public String encode(String message) {
    StringBuilder result = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            char base = Character.isUpperCase(c) ? 'A' : 'a';
            result.append((char) (base + ((c - base + 2) % 26)));
        } else {
            result.append(c);
        }
    }
    return result.toString();
}