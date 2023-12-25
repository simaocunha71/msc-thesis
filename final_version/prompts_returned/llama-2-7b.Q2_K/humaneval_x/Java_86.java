import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    antiShuffle("Hi") returns "Hi"
    antiShuffle("hello") returns "ehllo"
    antiShuffle("Hello World!!!") returns "Hello !!!Wdlor"
     */
    public String antiShuffle(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<s.length();i++){
            char chr = s.charAt(i);
            if((128 <= chr.getNumericValue() && chr <= 255))
                sb.append((byte)chr.getNumericValue());
        }
        return sb.toString();
    }
}