import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a message, and encodes in such a
    way that it swaps case of all letters, replaces all vowels in
    the message with the letter that appears 2 places ahead of that
    vowel in the english alphabet.
    Assume only letters.

    Examples:
    >>> encode("test")
    "TGST"
    >>> encode("This is a message")
    "tHKS KS C MGSSCGG"
     */
    public String encode(String message) {

        String encode = "";
        String lowerCase = message.toLowerCase();
        for (int i = 0; i < lowerCase.length(); i++) {
            if (lowerCase.charAt(i) == 'a' || lowerCase.charAt(i) == 'e' || lowerCase.charAt(i) == 'i' || lowerCase.charAt(i) == 'o' || lowerCase.charAt(i) == 'u') {
                encode += String.valueOf(lowerCase.charAt(i)).toUpperCase();
            } else if (lowerCase.charAt(i) == 'b' || lowerCase.charAt(i) == 'c' || lowerCase.charAt(i) == 'd' || lowerCase.charAt(i) == 'f' || lowerCase.charAt(i) == 'g') {
                encode += String.valueOf(lowerCase.charAt(i)).toLowerCase();
            } else {
                encode += lowerCase.charAt(i);
            }
        }
        return encode;
    }
}
