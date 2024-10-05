        MessageDigest md = MessageDigest.getInstance("MD5");

        if (text.isEmpty()) {
            return Optional.empty();
        }

        md.update(text.getBytes());
        byte[] digest = md.digest();
        String hashText = new BigInteger(1, digest).toString(16);

        while(hashText.length() < 32) {
            hashText = "0" + hashText;
        }

        return Optional.of(hashText);
    }
}

This solution uses MessageDigest to calculate the MD5 hash of the string. The hash is represented as a byte array, which is then converted to a hexadecimal string. If the resulting string's length is less than 32, it is padded with zeros on its left. The resulting string is then wrapped in an Optional object. If the input string is empty, an empty Optional is returned.

Please note that the MessageDigest class is considered to be a low-level class for computing message digests, and its use can be considered insecure. In fact, it may be possible to construct a MessageDigest instance that will not correctly verify the integrity of data, or to manipulate the data in a way that it will be accepted by the MessageDigest.

In other words, if you need to verify data integrity, consider using a more secure class such as java.security.MessageDigest.

This class is not meant to be used in situations where security is a concern, such as when you're dealing with sensitive user data.

Therefore, this solution is not suitable for use in a real-world application where security is a concern.
    */


A: import java.math.BigInteger;
import java.security.*;
import java.util.*;

class Solution {

    public static Optional<String> stringToMd5(String text) throws NoSuchAlgorithmException {

        MessageDigest md = MessageDigest.getInstance("MD5");

        if (text == null || text.isEmpty()) {
            return Optional.empty();
        }

        md.update(text.getBytes());
        byte[] digest = md.digest();
        String hashText = new BigInteger(1, digest).toString(1