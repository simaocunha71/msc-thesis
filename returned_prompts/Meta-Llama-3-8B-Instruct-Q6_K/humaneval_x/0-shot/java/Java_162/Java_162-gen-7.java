Here is the solution to the problem:

```java
import java.math.BigInteger;
import java.security.*;
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string "text", return its md5 hash equivalent string with length being 32.
    If "text" is an empty string, return Optional.empty().
    
    >>> stringToMd5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"
     */
    public Optional<String> stringToMd5(String text) throws NoSuchAlgorithmException {
        if (text == null || text.isEmpty()) {
            return Optional.empty();
        }

        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md.digest(text.getBytes());

        BigInteger bigInt = new BigInteger(1, hashBytes);
        String hashString = bigInt.toString(16);

        // Pad with leading zeros to make it 32 characters long
        while (hashString.length() < 32) {
            hashString = "0" + hashString;
        }

        return Optional.of(hashString);
    }
}
```

This solution first checks if the input string is null or empty. If it is, it returns an empty Optional. Otherwise, it uses the MessageDigest class to generate the MD5 hash of the input string. The hash is then converted to a BigInteger object and its hexadecimal representation is obtained. The resulting string is padded with leading zeros to make it 32 characters long, and then it is returned as an Optional.