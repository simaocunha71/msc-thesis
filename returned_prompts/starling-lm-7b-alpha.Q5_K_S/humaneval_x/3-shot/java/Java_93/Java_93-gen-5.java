        StringBuilder result = new StringBuilder();
        char[] message_chars = message.toCharArray();
        for (char c : message_chars) {
            if (Character.isUpperCase(c)) {
                result.append(Character.toLowerCase(c));
            } else if (Character.isLowerCase(c)) {
                result.append(Character.toUpperCase(c));
            } else if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                char new_c = (char) (c + 2);
                if (new_c > 'z') {
                    new_c -= 26;
                }
                result.append(new_c);
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

