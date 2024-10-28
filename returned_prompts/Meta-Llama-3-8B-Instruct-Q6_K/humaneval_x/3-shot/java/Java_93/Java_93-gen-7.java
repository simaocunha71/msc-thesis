        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char originalCase = Character.isUpperCase(c) ? 'U' : 'L';
                char newChar = Character.toUpperCase(c);
                if (newChar == 'a' || newChar == 'A') {
                    newChar = 'c';
                } else if (newChar == 'e' || newChar == 'E') {
                    newChar = 'g';
                } else if (newChar == 'i' || newChar == 'I') {
                    newChar = 'k';
                } else if (newChar == 'o' || newChar == 'O') {
                    newChar = 'q';
                } else if (newChar == 'u' || newChar == 'U') {
                    newChar = 'w';
                }
                if (originalCase == 'L') {
                    newChar = Character.toLowerCase(newChar);
                }
                result.append(newChar);
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}