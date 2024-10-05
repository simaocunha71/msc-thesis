        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    result.append((char) (c + 2));
                } else {
                    result.append((char) (c - 2));
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

