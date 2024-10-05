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

        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        char[] shifted = new char[alphabet.length];
        for (int i = 0; i < alphabet.length; i++) {
            shifted[i] = (char) (alphabet[i] + 2 * 2);
        }

        char[] encrypted = new char[s.length()];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            for (int j = 0; j < alphabet.length; j++) {
                if (c == alphabet[j]) {
                    encrypted[i] = shifted[j];
                    break;
                }
            }
        }
        return new String(encrypted);
    }
}
