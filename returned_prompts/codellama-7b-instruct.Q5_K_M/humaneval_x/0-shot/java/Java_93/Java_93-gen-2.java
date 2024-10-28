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
        int vowelIndex = 0;
        char[] chars = message.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] >= 'A' && chars[i] <= 'Z') {
                if (chars[i] == 'E' || chars[i] == 'I' || chars[i] == 'O' || chars[i] == 'U') {
                    chars[i] = (char) (chars[i] + vowelIndex);
                } else {
                    chars[i] = (char) (chars[i] - vowelIndex);
                }
            } else if (chars[i] >= 'a' && chars[i] <= 'z') {
                if (chars[i] == 'e' || chars[i] == 'i' || chars[i] == 'o' || chars[i] == 'u') {
                    chars[i] = (char) (chars[i] + vowelIndex);
                } else {
                    chars[i] = (char) (chars[i] - vowelIndex);
                }
            }
            encoded = encoded + chars[i];
        }
        return encoded;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        Solution sol = new Solution();
        String ret = sol.encode(s);
        System.out.println(ret);
