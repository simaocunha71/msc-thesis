        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    encodedMessage.append(Character.toUpperCase(c));
                } else {
                    encodedMessage.append(Character.toLowerCase(c));
                }
            } else if (c == 'a') {
                encodedMessage.append('C');
            } else if (c == 'e') {
                encodedMessage.append('G');
            } else if (c == 'i') {
                encodedMessage.append('K');
            } else if (c == 'o') {
                encodedMessage.append('Q');
            } else if (c == 'u') {
                encodedMessage.append('W');
            } else {
                encodedMessage.append(c);
            }
        }
        return encodedMessage.toString();
    }
}

