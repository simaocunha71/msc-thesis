        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    encodedMessage.append(Character.toUpperCase(c));
                } else {
                    encodedMessage.append(Character.toLowerCase(c));
                }
            } else {
                encodedMessage.append(c);
            }
        }

        for (int i = 0; i < encodedMessage.length(); i++) {
            char c = encodedMessage.charAt(i);
            if (Character.isLetter(c)) {
                if (isVowel(c)) {
                    char newChar = (char) (c + 2);
                    if (Character.isLowerCase(c) && newChar > 'z') {
                        newChar = (char) ('a' + newChar - 'z' - 1);
                    } else if (Character.isUpperCase(c) && newChar > 'Z') {
                        newChar = (char) ('A' + newChar - 'Z' - 1);
                    }
                    encodedMessage.setCharAt(i, newChar);
                }
            }
        }

        return encodedMessage.toString();
    }

    private boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

This program takes a string as input and replaces the lowercase characters with uppercase, and vice versa. It also replaces all vowels with the letter that appears 2 places ahead of that vowel in the English alphabet. The function isVowel checks if a character is a vowel.
This program has a time complexity of O(n) and a space complexity of O(n) as it iterates through the message twice.

*/

// Tests
class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.encode