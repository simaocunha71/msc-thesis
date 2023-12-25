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
        StringBuilder encoded = new StringBuilder();
        for (int i=0;i<message.length();++i){
            char c = message.charAt(i);
            // if the current character has a lowercase letter, try to find its uppercase counterpart and substitute it instead
            int j = c - 'a';
            while (j < 'z' && message.toLowerCase().indexOf((int)c, i) == -1){
                encoded.append('z').append(message.charAt(i));
                c -= 'a';
                j++;
                if (j >= 26 || message.toUpperCase().indexOf((int)c, i) == -1) break;
            } else {
                encoded.append((char)(c + 'a')).append(message.charAt(i));
            }
        }
        return encoded.toString();
    }
}
