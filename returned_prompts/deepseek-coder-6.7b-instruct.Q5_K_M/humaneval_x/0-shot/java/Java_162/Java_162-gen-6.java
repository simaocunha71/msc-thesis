        if (text == null || text.equals("")){
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] messageDigest = md.digest(text.getBytes());
        BigInteger no = new BigInteger(1, messageDigest);
        String hashtext = no.toString(16); 
        while (hashtext.length() < 32) { 
            hashtext = "0" + hashtext; 
        }
        return Optional.of(hashtext);
    }
}

The solution above converts a string to its MD5 hash equivalent and returns it as a string of length 32. It uses the MessageDigest class from java.security package to compute the MD5 hash of the input text. BigInteger class is used to convert byte array to hexadecimal string. The solution also handles an empty string case by returning an Optional.empty().

Test the solution with a string and print the result:

```java
public class Main {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        Solution solution = new Solution();
        Optional<String> hash = solution.stringToMd5("Hello world");
        if (hash.isPresent()) {
            System.out.println(hash.get());
        } else {
            System.out.println("Empty input string");
        }
    }
}
```

This will print:

```
3e25960a79dbc69b674cd4ec67a72c62
```

which is the MD5 hash of the string "Hello world".

Note: The solution assumes that the input string is not null. If it can be null, then a NullPointerException may occur in the code above.
*/

import java.util.*;
import java.math.BigInteger;
import java.security.*;

public class Main {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        Solution solution = new Solution();
        Optional<String> hash = solution.stringToMd5("Hello world");
        if (hash.isPresent()) {