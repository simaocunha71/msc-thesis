public class Main {
    public static void main(String[] args) {
        System.out.println(encode("test"));
        System.out.println(encode("This is a message"));
    }

    public static String encode(String message) {
        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isUpperCase(c)) {
                char lowerCaseChar = Character.toLowerCase(c);
                if (lowerCaseChar == 'a' || lowerCaseChar == 'e' || lowerCaseChar == 'i' || lowerCaseChar == 'o' || lowerCaseChar == 'u') {
                    encodedMessage.append((char) (lowerCaseChar + 2));
                } else {
                    encodedMessage.append(Character.toUpperCase((char) (lowerCaseChar + 2)));
                }
            } else {
                char upperCaseChar = Character.toUpperCase(c);
                if (upperCaseChar == 'A' || upperCaseChar == 'E' || upperCaseChar == 'I' || upperCaseChar == 'O' || upperCaseChar == 'U') {
                    encodedMessage.append((char) (upperCaseChar + 2));
                } else {
                    encodedMessage.append(Character.toLowerCase((char) (upperCaseChar + 2)));
                }
            }
        }
        return encodedMessage.toString();
    }
}