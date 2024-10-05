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
        if (text.isEmpty()) {
            return Optional.empty();
        }
        
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md.digest(text.getBytes());
        BigInteger bigInt = new BigInteger(1, hashBytes);
        String hashString = bigInt.toString(16);
        while (hashString.length() < 32) {
            hashString = "0" + hashString;
        }
        return Optional.of(hashString);
    }
}
```


In this solution, we first check if the input string is empty. If it is, we return Optional.empty(). 

Then, we create a MessageDigest object using the "MD5" algorithm. We use this object to generate the md5 hash of the input string. 

We convert the resulting byte array to a BigInteger object, which is a class in Java that represents a big integer. We use this object to convert the byte array to a string in hexadecimal format. 

Finally, we return the resulting string. If the string is shorter than 32 characters, we add leading zeros to make it 32 characters long. 

This solution should work correctly for any input string, including an empty string. It also returns the correct md5 hash for the input string "Hello world", which is "3e25960a79dbc69b674cd4ec67a72c62". 