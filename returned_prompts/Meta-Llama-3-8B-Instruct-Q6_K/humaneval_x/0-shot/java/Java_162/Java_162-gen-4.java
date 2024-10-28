Here is the Java code that calculates the MD5 hash of a given string and returns it as a 32-character string:

```java
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Optional;

public class Solution {
    public Optional<String> stringToMd5(String text) throws NoSuchAlgorithmException {
        if (text == null || text.isEmpty()) {
            return Optional.empty();
        }
        
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md.digest(text.getBytes());
        
        BigInteger num = new BigInteger(1, hashBytes);
        StringBuilder hexString = new StringBuilder(num.toString(16));
        
        while (hexString.length() < 32) {
            hexString.insert(0, '0');
        }
        
        return Optional.of(hexString.toString());
    }
}
```

This solution uses the `MessageDigest` class from the `java.security` package to calculate the MD5 hash of the given string. The hash is then converted to a `BigInteger` and formatted as a 32-character hexadecimal string. If the input string is empty, the method returns an empty `Optional`.

You can test this solution using the following code:

```java
public static void main(String[] args) throws NoSuchAlgorithmException {
    Solution solution = new Solution();
    System.out.println(solution.stringToMd5("Hello world"));
}
```

This will output the MD5 hash of the string "Hello world", which should be "3e25960a79dbc69b674cd4ec67a72c62". If you pass an empty string to the `stringToMd5` method, it will return an empty `Optional`.