        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    result.append((char) (c - 2));
                } else {
                    result.append((char) (c + 2));
                }
            } else {
                result.append(Character.toLowerCase(c));
            }
        }
        return result.toString();
    }
}

