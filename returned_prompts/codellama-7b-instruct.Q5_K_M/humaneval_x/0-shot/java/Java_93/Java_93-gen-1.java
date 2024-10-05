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
        char[] charMessage = message.toCharArray();

        for (int i = 0; i < charMessage.length; i++) {
            if (charMessage[i] >= 'a' && charMessage[i] <= 'z') {
                if (charMessage[i] == 'a' || charMessage[i] == 'e' || charMessage[i] == 'i' || charMessage[i] == 'o' || charMessage[i] == 'u') {
                    charMessage[i] = (char)((charMessage[i] + 2) % 26 + 'A');
                } else {
                    charMessage[i] = (char)((charMessage[i] - 2) % 26 + 'a');
                }
            } else if (charMessage[i] >= 'A' && charMessage[i] <= 'Z') {
                if (charMessage[i] == 'A' || charMessage[i] == 'E' || charMessage[i] == 'I' || charMessage[i] == 'O' || charMessage[i] == 'U') {
                    charMessage[i] = (char)((charMessage[i] - 2) % 26 + 'a');
                } else {
                    charMessage[i] = (char)((charMessage[i] + 2) % 26 + 'A');
                }
            }
        }
        return new String(charMessage);
    }
}
