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

        String[] words = s.split(" ");
        String[] orderedWords = new String[words.length];
        for(int i = 0; i < words.length; i++){
            char[] chars = words[i].toCharArray();
            Arrays.sort(chars);
            orderedWords[i] = new String(chars);
        }

        return String.join(" ", orderedWords);
    }
}