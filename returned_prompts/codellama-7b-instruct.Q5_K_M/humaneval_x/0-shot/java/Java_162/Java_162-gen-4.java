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
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes());
        byte[] bytes = md.digest();
        BigInteger bi = new BigInteger(1, bytes);
        String hash = bi.toString(16);
        while (hash.length() < 32) {
            hash = "0" + hash;
        }
        return Optional.of(hash);
    }
}

