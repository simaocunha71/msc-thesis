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

        // your code here
        if (text.equals("")) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] bytes = md.digest(text.getBytes());
        BigInteger bi = new BigInteger(bytes);
        String md5 = bi.toString(16);
        while (md5.length() < 32) {
            md5 = "0" + md5;
        }
        return Optional.of(md5);
    }
}