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
        // return s.replaceAll("[a-z]", m -> (char) (m.group() + 2)).toUpperCase();
        return s.replaceAll("[a-z]", m -> (char) (m.group() - 2)).toLowerCase();
    }
}
