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
        String encodedMessage = "";
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String vowels = "aeiou";

        for (int i = 0; i < message.length(); i++) {
            if (alphabet.contains(message.charAt(i) + "")) {
                if (vowels.contains(message.charAt(i) + "")) {
                    encodedMessage += uppercaseAlphabet.charAt(uppercaseAlphabet.indexOf(message.charAt(i)) + 2);
                } else {
                    encodedMessage += uppercaseAlphabet.charAt(uppercaseAlphabet.indexOf(message.charAt(i)) - 1);
                }
            } else {
                encodedMessage += message.charAt(i);
            }
        }

        return encodedMessage;
    }
}
