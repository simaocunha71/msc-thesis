import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated.
    The alphabet should be rotated in a manner such that the letters
    shift down by two multiplied to two places.
    For example:
    encrypt("hi") returns "lm"
    encrypt("asdfghjkl") returns "ewhjklnop"
    encrypt("gf") returns "kj"
    encrypt("et") returns "ix"
     */
    public String encrypt(String s) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < s.length(); i++) {
            int index = alphabet.indexOf(s.charAt(i));
            if (index != -1) {
                int newIndex = index + 2 * 2;
                if (newIndex >= alphabet.length()) {
                    newIndex -= alphabet.length();
                }
                sb.append(alphabet.charAt(newIndex));
            }
            else {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}
