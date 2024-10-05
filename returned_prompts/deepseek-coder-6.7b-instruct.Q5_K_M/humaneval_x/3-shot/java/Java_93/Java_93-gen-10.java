        StringBuilder encoded_message = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    encoded_message.append(Character.toUpperCase(c));
                } else {
                    encoded_message.append(Character.toLowerCase(c));
                }
            } else {
                encoded_message.append(c);
            }
        }
        return encoded_message.toString();
    }
}

