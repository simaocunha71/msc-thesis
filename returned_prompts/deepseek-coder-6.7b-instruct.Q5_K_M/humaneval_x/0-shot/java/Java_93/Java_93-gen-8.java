        StringBuilder result = new StringBuilder();
        for (char ch : message.toCharArray()) {
            if (Character.isAlphabetic(ch)) {
                if (Character.isLowerCase(ch)) {
                    result.append(Character.toUpperCase(ch));
                } else {
                    result.append(Character.toLowerCase(ch));
                }
            } else {
                result.append(ch);
            }
        }

        String newMessage = result.toString();
        result.setLength(0);

        for (char ch : newMessage.toCharArray()) {
            if (Character.isAlphabetic(ch)) {
                if (Character.toLowerCase(ch) == 'a') {
                    result.append('c');
                } else if (Character.toLowerCase(ch) == 'e') {
                    result.append('g');
                } else if (Character.toLowerCase(ch) == 'i') {
                    result.append('k');
                } else if (Character.toLowerCase(ch) == 'o') {
                    result.append('q');
                } else if (Character.toLowerCase(ch) == 'u') {
                    result.append('w');
                } else {
                    result.append(ch);
                }
            } else {
                result.append(ch);
            }
        }

        return result.toString();
    }

}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.encode("test")); // "TGST"
        System.out.println(solution.encode("This is a message")); // "tHKS KS C MGSSCGG"
    }
}

This is a solution in Java. It firstly swaps the case of all the letters in the message and then replaces all the vowels with the letter that appears 2 places ahead of that vowel in the English alphabet.

Please note that this solution assumes that the input message will only contain English alphabets and spaces. If the input message might contain special characters or