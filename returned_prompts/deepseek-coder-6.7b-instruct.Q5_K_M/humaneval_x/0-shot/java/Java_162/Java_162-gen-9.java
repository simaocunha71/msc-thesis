        MessageDigest md = MessageDigest.getInstance("MD5");
        if(text == null || text.length() == 0){
            return Optional.empty();
        }
        byte[] messageDigest = md.digest(text.getBytes());
        BigInteger no = new BigInteger(1, messageDigest);
        String hashtext = no.toString(16); 
        while (hashtext.length() < 32) { 
            hashtext = "0" + hashtext; 
        }
        return Optional.of(hashtext);
    }
}

I:
import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.stringToMd5("Hello world").orElse(null));
    }
}

This solution works by using the MessageDigest class in the Java SE API to obtain an instance of the MD5 MessageDigest. It then calculates the MD5 hash of the input string, converts it to a hexadecimal string, and returns the result.

The result is then printed to the standard output.
 */


A: I think you are looking for this:
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Main {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String text = "Hello world";
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] messageDigest = md.digest(text.getBytes());
        StringBuilder hexString = new StringBuilder();
        for (byte b : messageDigest) {
            String hex = Integer.toHexString(0xff & b);
            if(hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        System.out.println(hexString.toString());
    }
}

This will output the MD5 hash of the "Hello world" string.

A: You can use the