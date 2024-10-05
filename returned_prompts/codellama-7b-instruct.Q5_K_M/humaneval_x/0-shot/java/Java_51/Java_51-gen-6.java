import java.util.*;
import java.lang.*;

class Solution {
    /**
    removeVowels is a function that takes string and returns string without vowels.
    >>> removeVowels("")
    ""
    >>> removeVowels("abcdef\nghijklm")
    "bcdf\nghjklm"
    >>> removeVowels("abcdef")
    "bcdf"
    >>> removeVowels("aaaaa")
    ""
    >>> removeVowels("aaBAA")
    "B"
    >>> removeVowels("zbcd")
    "zbcd"
     */
    public String removeVowels(String text) {

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == 'a' || text.charAt(i) == 'e' || text.charAt(i) == 'i' || text.charAt(i) == 'o' || text.charAt(i) == 'u') {
                continue;
            } else {
                builder.append(text.charAt(i));
            }
        }
        return builder.toString();
    }
}

class Solution {
    /**
    removeVowels is a function that takes string and returns string without vowels.
    >>> removeVowels("")
    ""
    >>> removeVowels("abcdef\nghijklm")
    "bcdf\nghjklm"
    >>> removeVowels("abcdef")
    "bcdf"
    >>> removeVowels("aaaaa")
    ""
    >>> removeVowels("aaBAA")
    "B"
    >>> removeVowels("zbcd")
    "zbcd"
     */
    public String removeVowels(String text) {

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == 'a' || text.charAt(i) == 'e' || text.charAt(i) == '