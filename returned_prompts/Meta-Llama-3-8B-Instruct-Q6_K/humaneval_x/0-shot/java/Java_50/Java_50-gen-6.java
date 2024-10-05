import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "hello";
        String encoded = solution.encodeShift(s);
        System.out.println("Encoded: " + encoded);
        String decoded = solution.decodeShift(encoded);
        System.out.println("Decoded: " + decoded);
    }
}

Solution.java:
```java
class Solution {
    /**
    returns encoded string by shifting every character by 5 in the alphabet.
     */
    public String encodeShift(String s) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch + 5 - 'a') % 26)));
        }
        return sb.toString();
    }

    /**
    takes as input string encoded with encodeShift function. Returns decoded string.
     */
    public String decodeShift(String s) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch - 5 - 'a') % 26)));
        }
        return sb.toString();
    }
}
```

Explanation:

1. The `encodeShift` method takes a string as input and returns the encoded string by shifting every character by 5 in the alphabet. It uses a `StringBuilder` object to append the encoded characters to a string.
2. The `decodeShift` method takes a string as input, which is assumed to be encoded with the `encodeShift` method. It returns the decoded string by shifting every character back by 5 in the alphabet. It uses a `StringBuilder` object to append the decoded characters to a string.
3. In the `encodeShift` method, the character is shifted by adding 5 to its ASCII value and taking the result modulo 26 (the number of letters in the alphabet). This ensures that the shifted character wraps around the alphabet if it exceeds 'z'.
4. In the `decodeShift` method, the character is shifted back by subtracting 5 from its ASCII value and taking the result modulo 26. This also ensures that the shifted character wraps around the alphabet if it goes below 'a'.
5. In the `main` method, we create a `Solution` object and call the `encodeShift` method to encode the string "hello". We then call the `decodeShift` method to decode the encoded string. The decoded string is printed to the console.

Output:
``