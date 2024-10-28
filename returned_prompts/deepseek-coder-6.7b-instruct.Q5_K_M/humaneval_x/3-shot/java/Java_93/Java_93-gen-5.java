        StringBuilder encoded_message = new StringBuilder(message.length());
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    encoded_message.append(Character.toUpperCase(c));
                } else {
                    encoded_message.append(Character.toLowerCase(c));
                }
            } else if ("aeiouAEIOU".indexOf(c) != -1) {
                if (Character.isLowerCase(c)) {
                    encoded_message.append((char) ('y' + c));
                } else {
                    encoded_message.append((char) ('Y' + c));
                }
            } else {
                encoded_message.append(c);
            }
        }
        return encoded_message.toString();
    }
}

