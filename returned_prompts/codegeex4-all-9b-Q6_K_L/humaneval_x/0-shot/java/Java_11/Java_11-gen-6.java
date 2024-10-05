You can perform the XOR operation between the two strings by using the caret (^) operator. Here is the code:

```java
public String stringXor(String a, String b) {
    if (a.length() != b.length()) {
        throw new IllegalArgumentException("Strings must be of the same length");
    }
    
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < a.length(); i++) {
        char c = (char) (a.charAt(i) ^ b.charAt(i));
        result.append(c);
    }
    
    return result.toString();
}
```

This code first checks if the two strings are of the same length. If not, it throws an `IllegalArgumentException`. 

Then it creates a `StringBuilder` object to store the result. It iterates over the characters of the strings and performs the XOR operation between them using the caret (^) operator. The result is appended to the `StringBuilder` object. 

Finally, the `StringBuilder` object is converted to a string using the `toString()` method and returned.