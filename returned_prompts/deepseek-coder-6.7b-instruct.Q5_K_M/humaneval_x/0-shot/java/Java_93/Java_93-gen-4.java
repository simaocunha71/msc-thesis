        StringBuilder sb = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    sb.append(Character.toUpperCase(c));
                } else {
                    sb.append(Character.toLowerCase(c));
                }
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}



A: You can solve this by iterating over the characters of the string and checking if they are vowels. If they are, replace them with the character that appears 2 places ahead in the alphabet. Also, swap the case of all characters.

Here's a possible solution:

```java
class Solution {
    public String encode(String message) {
        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (isVowel(c)) {
                    encodedMessage.append(shiftAlphabet(c, 2));
                } else {
                    encodedMessage.append(Character.isLowerCase(c) ? Character.toUpperCase(c) : Character.toLowerCase(c));
                }
            } else {
                encodedMessage.append(c);
            }
        }
        return encodedMessage.toString();
    }

    private boolean isVowel(char c) {
        return "AEIOUaeiou".indexOf(c) != -1;
    }

    private char shiftAlphabet(char c, int shift) {
        int asciiOffset = Character.isUpperCase(c) ? 65 : 97;
        return (char)((c - asciiOffset + shift) % 26 + asciiOffset);
    }
}
```

This solution uses the `StringBuilder` class to efficiently build the encoded message. The `isVowel` method checks if a character is a vowel. The `shiftAlphabet` method shifts a character in the alphabet by a certain number of positions.

The `