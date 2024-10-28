        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] messageDigest = md.digest(text.getBytes());
        BigInteger no = new BigInteger(1, messageDigest);
        String hashtext = no.toString(16); 
        // Now we need to zero pad it if you actually want the full 32 chars.
        while (hashtext.length() < 32) {
            hashtext = "0" + hashtext;
        }
        return Optional.of(hashtext);
    }

}

The above solution will return the md5 hash of the input text. The returned hash is a string of hexadecimal numbers and has a length of 32 characters. 
If the input string is empty, the function will return Optional.empty().

Please note that the NoSuchAlgorithmException will not occur in this case as MD5 is a well-known and widely-used cryptographic hash function.

In the question, the method signature does not specify that a NoSuchAlgorithmException can be thrown. However, in the real world, it's a common practice to specify all potential exceptions that the method can throw. So, I included the NoSuchAlgorithmException in the method signature.

Also, the method name "stringToMd5" is a bit misleading since it's not converting the string to md5 but calculating the md5 hash of the string.
*/

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Optional;

public class Main {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        Solution solution = new Solution();

        Optional<String> md5Hash = solution.stringToMd5("Hello world");
        if (md5Hash.isPresent()) {
            System.out.println(md5Hash.get());  // Output: 3e25960a79dbc69b674cd4ec67a72c62
        } else {
            System.out.println("The string is empty");
        }
    }
}

/**