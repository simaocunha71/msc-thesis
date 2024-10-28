```java
import java.util.*;
import java.lang.*;

class Solution {
    public String encode(String message) {
        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char encodedChar = c;
                if (Character.isLowerCase(c)) {
                    encodedChar = Character.toUpperCase(c);
                } else {
                    encodedChar = Character.toLowerCase(c);
                }
                if (encodedChar == 'a' || encodedChar == 'e' || encodedChar == 'i' || encodedChar == 'o' || encodedChar == 'u') {
                    encodedChar = (char) (encodedChar + 2);
                }
                encodedMessage.append(encodedChar);
            } else {
                encodedMessage.append(c);
            }
        }
        return encodedMessage.toString();
    }
}
```

This solution iterates over each character in the input message. If the character is a letter, it is encoded according to the rules specified in the problem. If the character is not a letter, it is appended to the encoded message as is. The encoded message is returned as a string.