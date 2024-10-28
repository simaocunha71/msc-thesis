import java.util.*;

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
        String result = "";
        for (String word : words) {
            char[] wordChars = word.toCharArray();
            Arrays.sort(wordChars);
            result += new String(wordChars);
        }
        return result;
    }
}
