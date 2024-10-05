        StringBuilder result = new StringBuilder();

        for (char c : message.toCharArray()) {
            char encoded_char = c;

            if (Character.isUpperCase(c)) {
                encoded_char = Character.toLowerCase(c);
            } else if (Character.isLowerCase(c)) {
                encoded_char = Character.toUpperCase(c);
            }

            if (encoded_char == 'a') {
                encoded_char = 'c';
            } else if (encoded_char == 'e') {
                encoded_char = 'g';
            } else if (encoded_char == 'i') {
                encoded_char = 'k';
            } else if (encoded_char == 'o') {
                encoded_char = 'q';
            } else if (encoded_char == 'u') {
                encoded_char = 'w';
            }

            result.append(encoded_char);
        }
        return result.toString();
    }
}

