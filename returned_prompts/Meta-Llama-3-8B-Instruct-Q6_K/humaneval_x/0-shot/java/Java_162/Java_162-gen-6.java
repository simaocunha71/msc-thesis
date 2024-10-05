The task is to create a function that takes a string as input and returns its MD5 hash equivalent string with a length of 32. If the input string is empty, the function should return an empty optional.

Here is the Java solution for the problem:

```java
import java.math.BigInteger;
import java.security.*;
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<String> stringToMd5(String text) throws NoSuchAlgorithmException {
        if (text == null || text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digest = md.digest(text.getBytes());
        BigInteger no = new BigInteger(1, digest);
        String hash = String.format("%032x", no);
        return Optional.of(hash);
    }
}
```

In this solution, we first check if the input string is null or empty. If it is, we return an empty optional. Otherwise, we get the MD5 hash of the string using the `MessageDigest` class. We then convert the hash to a big integer and format it as a 32-character hexadecimal string. Finally, we return an optional containing the hash string.