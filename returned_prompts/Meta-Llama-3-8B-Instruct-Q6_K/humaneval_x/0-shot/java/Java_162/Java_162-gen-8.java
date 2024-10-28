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
        BigInteger hashBigInt = new BigInteger(1, hashBytes);
        String hashString = hashBigInt.toString(16).toUpperCase();

        while (hashString.length() < 32) {
            hashString = "0" + hashString;
        }

        return Optional.of(hashString);
    }
}
```

The function `stringToMd5` first checks if the input string `text` is null or empty. If it is, the function returns an empty optional.

Then, it creates a `MessageDigest` object using the MD5 algorithm and digests the input string `text` using the `digest` method. The result is an array of bytes representing the MD5 hash of the input string.

Next, it converts the byte array to a `BigInteger` object using the `BigInteger` constructor with the radix 16 (hexadecimal). The `BigInteger` object represents the MD5 hash as a hexadecimal string.

The function then converts the `BigInteger` object to a string using the `toString` method with the radix 16 (hexadecimal). The resulting string is the MD5 hash of the input string in hexadecimal format.

Finally, the function returns an optional string containing the MD5 hash. If the input string is empty, the function returns an empty optional. Otherwise, it returns an optional containing the MD5 hash. The length of the MD5 hash is 32 characters, which is the standard length for an MD5 hash. If the MD5 hash has less than 32 characters, the function pads it with leading zeros to make it 32 characters long.