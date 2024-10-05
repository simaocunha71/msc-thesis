        StringBuilder sb = new StringBuilder();
        for (char ch: s.toCharArray()) {
            sb.append((char) ('a' + ((ch - 5 - 'a' + 26) % 26)));
        }
        return sb.toString();
    }
}

```

The function encodeShift works by shifting the ASCII value of each character in the input string by 5. The decodeShift function then reverses this encoding by shifting the ASCII value of each character in the input string by -5. In both cases, the modulo operation is used to ensure that the resulting character is still within the range of valid ASCII characters (a-z).

Here's the test code:

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        String original = "hello";
        String encoded = solution.encodeShift(original);
        String decoded = solution.decodeShift(encoded);

        System.out.println("Original: " + original);
        System.out.println("Encoded: " + encoded);
        System.out.println("Decoded: " + decoded);
    }
}
```

This should output:

```
Original: hello
Encoded: mjqqt
Decoded: hello
```

As you can see, the encoded string "mjqqt" is obtained by shifting each character in "hello" by 5 in the alphabet, and the decoded string "hello" is the original string.

Please note that this solution only works for lowercase letters and does not handle uppercase letters or any other characters. If you want to handle uppercase letters or other characters, you would need to modify the solution to handle these cases.










































































































