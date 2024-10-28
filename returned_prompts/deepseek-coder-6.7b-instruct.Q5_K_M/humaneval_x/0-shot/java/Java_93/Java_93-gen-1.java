        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    char newChar = (char) (c - 32);
                    result.append(newChar);
                } else {
                    char newChar = (char) (c + 32);
                    result.append(newChar);
                }
            } else {
                result.append(c);
            }
        }

        String resultString = result.toString();
        for (int i = 0; i < resultString.length(); i++) {
            char c = resultString.charAt(i);
            if (isVowel(c)) {
                if (Character.isLowerCase(c)) {
                    char newChar = (char) (c + 2);
                    if (newChar > 'z') {
                        newChar = (char) (newChar - 26);
                    }
                    result.setCharAt(i, newChar);
                } else {
                    char newChar = (char) (c + 2);
                    if (newChar > 'Z') {
                        newChar = (char) (newChar - 26);
                    }
                    result.setCharAt(i, newChar);
                }
            }
        }
        return result.toString();
    }

    private boolean isVowel(char c) {
        return "AEIOUaeiou".indexOf(c) != -1;
    }
}

This solution iterates through the input message. If a character is a letter, it swaps its case, appends it to the result. If it's not a letter, it just appends it to the result as it is.
After that, it goes through the result string again. If a character is a vowel, it finds the character that appears 2 places ahead in the alphabet (considering 'z' or 'Z' as the first character after 'y' or 'Y') and replaces the vowel with this character.
Finally, it returns the encoded message.

Please note that this solution assumes that the input message only contains English