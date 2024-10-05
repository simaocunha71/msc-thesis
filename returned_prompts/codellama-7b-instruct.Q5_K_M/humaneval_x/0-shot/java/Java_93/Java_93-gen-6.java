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
        String result = "";
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (c >= 'a' && c <= 'z') {
                result += (char) (c - 32);
            } else if (c >= 'A' && c <= 'Z') {
                result += (char) (c + 32);
            } else if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                result += (char) (c + 2);
            } else {
                result += c;
            }
        }
        return result;
    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> sortedSquares(int[] A) {
        int[] temp = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            temp[i] = A[i] * A[i];
        }
        Arrays.sort(temp);
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < temp.length; i++) {
            result.add(temp[i]);
        }
        return result;
    }
}

import java.util.Arrays;

class Solution {
    public int[] sortedS