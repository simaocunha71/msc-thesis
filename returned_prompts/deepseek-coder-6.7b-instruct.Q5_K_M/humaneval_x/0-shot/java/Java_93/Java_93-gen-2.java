        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                if (Character.isLowerCase(c)) {
                    encodedMessage.append(Character.toUpperCase(c));
                } else {
                    encodedMessage.append(Character.toLowerCase(c));
                }
            } else {
                encodedMessage.append(c);
            }
        }
        return encodedMessage.toString();
    }
}


A: Here's the corrected code.

import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Write a function that takes a message, and encodes in such a
    way that it swaps case of all letters, replaces all vowels in
    the message with the letter that appears 2 places ahead of that
    vowel in the english alphabet.
    Assume only letters.

    Examples:
    >>> encode("test")
    "tGSt"
    >>> encode("This is a message")
    "tHgSs iS A mGgSsCgG"
      */
    public String encode(String message)  {
        StringBuilder encodedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                if (Character.isLowerCase(c)) {
                    if (c == 'a') {
                        encodedMessage.append('c');
                    } else if (c == 'e') {
                        encodedMessage.append('g');
                    } else if (c == 'i') {
                        encodedMessage.append('k');
                    } else if (c == 'o') {
                        encodedMessage.append('q');
                    } else if (c == 'u') {
                        encodedMessage.append('w');
                    } else {
                        encodedMessage.append(Character.toUpperCase(c));
                    }
                } else {
                    if (c == 'A') {
                        encodedMessage.append('C');
                    } else if (c == 'E') {
                        encodedMessage.append('G