        StringBuilder encoded = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                if (Character.isLowerCase(c)) {
                    encoded.append(Character.toUpperCase(c));
                } else {
                    encoded.append(Character.toLowerCase(c));
                }
            } else {
                encoded.append(c);
            }
        }
        return encoded.toString();
    }
}

