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
        byte[] messageDigest = md.digest(text.getBytes());
        BigInteger no = new BigInteger(1, messageDigest);
        StringBuilder hashtext = new StringBuilder(no.toString(16));
        while (hashtext.length() < 32) {
            hashtext.insert(0, "0");
        }
        return Optional.of(hashtext.toString());
    }
}
```