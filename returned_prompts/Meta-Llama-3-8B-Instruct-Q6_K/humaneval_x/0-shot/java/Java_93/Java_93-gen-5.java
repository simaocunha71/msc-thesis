    public String encode(String message) {
        StringBuilder result = new StringBuilder();

        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    result.append((char) ('a' + (c - 'A')));
                } else {
                    result.append((char) ('A' + (c - 'a')));
                }
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    result.append((char) (c + 2));
                }
            } else {
                result.append(c);
            }
        }

        return result.toString();
    }

