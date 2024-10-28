```java
import java.util.*;
import java.lang.*;

class Solution {
    public String encrypt(String s) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String encryptedAlphabet = alphabet.substring(4) + alphabet.substring(0, 4);
        StringBuilder encryptedString = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                char encryptedChar = encryptedAlphabet.charAt(alphabet.indexOf(Character.toLowerCase(c)));
                encryptedString.append(Character.isUpperCase(c) ? Character.toUpperCase(encryptedChar) : encryptedChar);
            } else {
                encryptedString.append(c);
            }
        }
        return encryptedString.toString();
    }
}
```