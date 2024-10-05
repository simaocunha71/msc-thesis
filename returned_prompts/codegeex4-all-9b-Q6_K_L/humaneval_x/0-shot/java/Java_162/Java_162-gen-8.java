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
        md.update(text.getBytes());
        byte[] digest = md.digest();

        BigInteger bigInt = new BigInteger(1, digest);
        String md5Hash = bigInt.toString(16);

        while (md5Hash.length() < 32) {
            md5Hash = "0" + md5Hash;
        }

        return Optional.of(md5Hash);
    }
}