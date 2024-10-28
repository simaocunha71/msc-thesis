        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    result.append((char) (c + 32));
                } else {
                    result.append((char) (c - 32));
                }

                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    result.append((char) ((c - 96 + 2) % 26 + 96));
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

