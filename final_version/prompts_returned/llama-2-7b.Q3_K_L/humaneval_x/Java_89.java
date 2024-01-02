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
        char[] ch = s.toCharArray();
        for (int i = 0;i<ch.length;i++) {
            if ((i+2) % 5 == 0 && i != 0)
                ch[i] -= 1;
        }
        StringBuilder sb = new StringBuilder(s);
        for (char c : ch) {
            sb.append((char)(c - 'a'+4));
        }
        return sb.toString();
    }
}