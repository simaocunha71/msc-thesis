import java.util.*;
import java.lang.*;

class Solution {
    public String encrypt(String s) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String rotatedAlphabet = "cdefghijklmnopqrstuvwxyzab";
        String encryptedString = "";
        for (int i = 0; i < s.length(); i++) {
            int currentIndex = alphabet.indexOf(s.charAt(i));
            encryptedString += rotatedAlphabet.charAt(currentIndex);
        }
        return encryptedString;
    }
}
