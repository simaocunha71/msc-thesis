Here is a solution to the problem:

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
        if (text.isEmpty()) {
            return Optional.empty();
        }
        
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md.digest(text.getBytes());
        
        BigInteger bigInt = new BigInteger(1, hashBytes);
        String hashText = bigInt.toString(16);
        
        while (hashText.length() < 32) {
            hashText = "0" + hashText;
        }
        
        return Optional.of(hashText);
    }
}
```

This solution uses the MessageDigest class to calculate the MD5 hash of the input string. The hash is then converted to a hexadecimal string using the BigInteger class. The resulting string is padded with leading zeros to ensure it has a length of 32. If the input string is empty, the method returns an empty Optional.

The unit test `>>> stringToMd5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"` ensures that the method returns the correct MD5 hash for the input string "Hello world". This test is written in Python, but the method itself is written in Java. The test can be run in a Python environment with a Java interpreter installed.