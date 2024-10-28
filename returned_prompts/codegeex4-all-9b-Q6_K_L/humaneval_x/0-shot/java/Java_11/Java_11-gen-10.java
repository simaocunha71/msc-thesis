```java
public String stringXor(String a, String b) {
    // Check if the input strings are of the same length
    if (a.length() != b.length()) {
        throw new IllegalArgumentException("Input strings must be of the same length");
    }

    StringBuilder result = new StringBuilder();

    // Perform binary XOR on each character
    for (int i = 0; i < a.length(); i++) {
        char charA = a.charAt(i);
        char charB = b.charAt(i);

        if (charA == charB) {
            result.append('0');
        } else {
            result.append('1');
        }
    }

    return result.toString();
}
```

Explanation:

1. We first check if the input strings are of the same length. If not, we throw an `IllegalArgumentException`.
2. We create a `StringBuilder` to store the result of the XOR operation.
3. We iterate over each character in the input strings.
4. For each character, we compare it with the corresponding character in the other string.
5. If the characters are the same, we append '0' to the result string. If they are different, we append '1'.
6. Finally, we return the result string.