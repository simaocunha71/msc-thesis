```java
public String encode(String message) {
    StringBuilder encodedMessage = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            char newChar;
            if (Character.isUpperCase(c)) {
                newChar = (char) (c + 32); // Convert to lowercase
                if (newChar == 'a' || newChar == 'e' || newChar == 'i' || newChar == 'o' || newChar == 'u') {
                    newChar = (char) (newChar + 2); // Move 2 places forward
                    if (newChar > 'z') {
                        newChar = (char) (newChar - 26); // Wrap around to 'a' if necessary
                    }
                }
            } else {
                newChar = (char) (c - 32); // Convert to uppercase
                if (newChar == 'a' || newChar == 'e' || newChar == 'i' || newChar == 'o' || newChar == 'u') {
                    newChar = (char) (newChar + 2); // Move 2 places forward
                    if (newChar > 'Z') {
                        newChar = (char) (newChar - 26); // Wrap around to 'A' if necessary
                    }
                }
            }
            encodedMessage.append(newChar);
        } else {
            encodedMessage.append(c);
        }
    }
    return encodedMessage.toString();
}
```

This function iterates over each character in the input message. If the character is a letter, it checks if it's uppercase or lowercase, and then applies the necessary transformations to swap the case and move the vowel two positions forward. If the character is not a letter, it's appended to the encoded message as is. The function returns the encoded message as a string.