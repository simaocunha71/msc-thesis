Here is a Java solution to the problem:

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

        BigInteger hash = new BigInteger(1, hashBytes);
        return Optional.of(hash.toString(16).toUpperCase());
    }
}
```

This solution uses the `MessageDigest` class to compute the MD5 hash of the input string. It first checks if the input string is null or empty, and if so, returns an empty `Optional`. If the input string is not empty, it computes the MD5 hash, converts the hash bytes to a BigInteger, and then converts the BigInteger to a string in hexadecimal format using the `toString(16)` method. The resulting string is then returned as an `Optional`. The `toUpperCase()` method is used to ensure that the output string is in uppercase.  The `NoSuchAlgorithmException` is thrown if the MD5 algorithm is not available.