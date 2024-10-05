        MessageDigest md = MessageDigest.getInstance("MD5");
        if(text.isEmpty()){
            return Optional.empty();
        } else {
            md.update(text.getBytes(), 0, text.length());
            return Optional.of(new BigInteger(1, md.digest()).toString(16));
        }
    }
}


A: You can use the MessageDigest class to generate MD5 hash.
Here is how you can do it:
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String text = "Hello world";
        System.out.println(stringToMd5(text));
    }

    public static String stringToMd5(String text) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] messageDigest = md.digest(text.getBytes());
        BigInteger no = new BigInteger(1, messageDigest);
        String hashtext = no.toString(16);
        while (hashtext.length() < 32) { 
            hashtext = "0" + hashtext; 
        }
        return hashtext;
    }
}

This will output:
3e25960a79dbc69b674cd4ec67a72c62

The MessageDigest class is used for creating the MD5 hash. We then convert the byte array to a BigInteger and then convert it to a hexadecimal string. The while loop is used to pad the string with zeros until it's length is 32.

A: This is the complete code.
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Main {
    public static void main(String[] args) {
        String text = "Hello world";
        try {
            System.out.println(stringToMd5(text));
        } catch (NoSuchAlgorithmException