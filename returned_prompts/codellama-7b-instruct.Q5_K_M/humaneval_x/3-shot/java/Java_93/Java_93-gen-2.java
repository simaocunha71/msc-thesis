        StringBuilder result = new StringBuilder();
        int i = 0;
        while (i < message.length()) {
            char c = message.charAt(i);
            if (c >= 'a' && c <= 'z') {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    result.append((char) (c + 2));
                } else {
                    result.append((char) (c - 2));
                }
            } else {
                result.append((char) (c - 32));
            }
            i += 1;
        }
        return result.toString();
    }
}

