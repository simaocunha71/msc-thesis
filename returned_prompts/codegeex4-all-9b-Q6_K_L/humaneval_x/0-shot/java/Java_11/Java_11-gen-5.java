```java
public String stringXor(String a, String b) {
    char[] result = new char[a.length()];
    for (int i = 0; i < a.length(); i++) {
        result[i] = (char) (a.charAt(i) ^ b.charAt(i));
    }
    return new String(result);
}
```

This solution uses the XOR operator (^) to perform binary XOR on the characters of the input strings. The result is stored in a character array, which is then converted back to a string and returned.