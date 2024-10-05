    public String encode(String message) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    result.append((char) (c + 32)); // lowercase
                } else {
                    result.append((char) (c - 32)); // uppercase
                }
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    result.append((char) ((c - 97 + 2) % 26 + 97)); // replace with next vowel
                } else {
                    result.append(c);
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }