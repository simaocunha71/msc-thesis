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
        String encoded = "";

        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (Character.isUpperCase(c)) {
                encoded += Character.toLowerCase(c);
            } else {
                encoded += Character.toUpperCase(c);
            }
        }

        for (int i = 0; i < encoded.length(); i++) {
            char c = encoded.charAt(i);
            if (Character.isLetter(c) &&
                Character.isVowel(c)) {
                int pos = Character.toUpperCase(c) - 65 + 2;
                if (pos >= 26) {
                    pos -= 26;
                }
                encoded = encoded.substring(0, i) +
                    (char) (pos + 65) +
                    encoded.substring(i + 1);
            }
        }
        return encoded;
    }
}
