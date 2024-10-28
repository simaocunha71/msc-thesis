        StringBuilder encodedMessage = new StringBuilder();

        for(char c : message.toCharArray()) {
            if(Character.isLetter(c)) {
                if(Character.isLowerCase(c)) {
                    encodedMessage.append(Character.toUpperCase(c));
                } else {
                    encodedMessage.append(Character.toLowerCase(c));
                }
            } else {
                encodedMessage.append(c);
            }
        }

        for(int i = 0; i < encodedMessage.length(); i++) {
            char c = encodedMessage.charAt(i);
            if(Character.isLetter(c) && "AEIOUaeiou".indexOf(c) != -1) {
                if(Character.isLowerCase(c)) {
                    encodedMessage.setCharAt(i, (char) ('c' + 1));
                } else {
                    encodedMessage.setCharAt(i, (char) ('C' + 1));
                }
            }
        }

        return encodedMessage.toString();
    }
}

