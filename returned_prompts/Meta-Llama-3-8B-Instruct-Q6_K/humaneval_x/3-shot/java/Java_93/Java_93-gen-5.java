        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char original = Character.toLowerCase(c);
                if (original == 'a' || original == 'e' || original == 'i' || original == 'o' || original == 'u') {
                    result.append((char) (original + 2));
                } else {
                    result.append(Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c));
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

