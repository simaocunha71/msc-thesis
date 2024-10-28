Here is the Java code to solve the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String encode(String message) {
        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                        encodedMessage.append((char) (c + 2));
                    } else {
                        encodedMessage.append(Character.toLowerCase(c));
                    }
                } else {
                    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                        encodedMessage.append((char) (c + 2));
                    } else {
                        encodedMessage.append(Character.toUpperCase(c));
                    }
                }
            } else {
                encodedMessage.append(c);
            }
        }
        return encodedMessage.toString();
    }
}
```
The code works as follows:

- It iterates over each character in the message.
- If the character is a letter, it checks if it is uppercase or lowercase.
- If the character is a vowel, it replaces it with the letter two places ahead in the alphabet.
- If the character is not a vowel, it simply swaps its case.
- If the character is not a letter, it is appended to the encoded message as is.