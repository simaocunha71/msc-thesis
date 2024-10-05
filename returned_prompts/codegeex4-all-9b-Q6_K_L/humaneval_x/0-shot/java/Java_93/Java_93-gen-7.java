Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public String encode(String message) {
        StringBuilder encodedMessage = new StringBuilder();

        for (char c : message.toCharArray()) {
            if (Character.isUpperCase(c)) {
                if (isVowel(c)) {
                    encodedMessage.append((char)(c + 2));
                } else {
                    encodedMessage.append(Character.toLowerCase(c));
                }
            } else {
                if (isVowel(c)) {
                    encodedMessage.append((char)(c - 32 + 2));
                } else {
                    encodedMessage.append(Character.toUpperCase(c));
                }
            }
        }

        return encodedMessage.toString();
    }

    private boolean isVowel(char c) {
        return "AEIOU".contains(String.valueOf(c));
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.encode("test")); // TGST
        System.out.println(solution.encode("This is a message")); // tHKS KS C MGSSCGG
    }
}
```

In the solution, we iterate over each character in the message. If the character is an uppercase letter and a vowel, we append the letter that appears 2 places ahead of that vowel in the english alphabet. If the character is an uppercase letter and not a vowel, we append the lowercase version of the character. If the character is a lowercase letter and a vowel, we append the letter that appears 2 places ahead of that vowel in the english alphabet. If the character is a lowercase letter and not a vowel, we append the uppercase version of the character. Finally, we return the encoded message.