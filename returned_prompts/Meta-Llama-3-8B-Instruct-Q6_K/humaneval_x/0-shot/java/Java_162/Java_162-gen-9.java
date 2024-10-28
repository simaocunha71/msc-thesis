Here is the solution:

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
        
        // Pad with leading zeros if necessary
        while (hashString.length() < 32) {
            hashString = "0" + hashString;
        }
        
        return Optional.of(hashString);
    }
}
```
In this solution, we use the `MessageDigest` class to generate the MD5 hash of the input string. We then convert the hash bytes to a `BigInteger` object and use its `toString` method to convert it to a hexadecimal string. We pad the string with leading zeros if necessary to ensure it has a length of 32. Finally, we return the resulting string as an `Optional` value. If the input string is empty, we return an empty `Optional` value.