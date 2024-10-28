Here is the solution:
```java
import java.math.BigInteger;
import java.security.*;
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<String> stringToMd5(String text) throws NoSuchAlgorithmException {
        if (text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] bytes = text.getBytes();
        byte[] hashBytes = md.digest(bytes);
        BigInteger bigInt = new BigInteger(1, hashBytes);
        String md5 = bigInt.toString(16);
        return Optional.of(md5);
    }
}
```
The solution uses the MessageDigest class from the java.security package to calculate the MD5 hash of the input string. It first checks if the input string is empty and returns Optional.empty() if it is. Then it creates a MessageDigest object with the MD5 algorithm, converts the input string to bytes, and digests the bytes to get the hash bytes. The hash bytes are then converted to a BigInteger object, which is then converted to a 16-digit hexadecimal string. This string is then returned as the MD5 hash equivalent of the input string. The solution uses Optional to return the result, which can be empty if the input string is empty.