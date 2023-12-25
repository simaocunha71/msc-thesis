import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that returns true if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and false otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    checkIfLastCharIsALetter("apple pie") -> false
    checkIfLastCharIsALetter("apple pi e") -> true
    checkIfLastCharIsALetter("apple pi e ") -> false
    checkIfLastCharIsALetter("") -> false
     */
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt.length() == 0) return false;
         Map<Character, Long> charToCount = new HashMap<>();
         List<Character> chars = Arrays.stream(txt).collect(Collectors.toList());
      //  System.out.println("count for A is " + charToCount.get('A'));
       return chars.removeLast().charValue() > -1 && !chars.stream().anyMatch((c) -> c == ' ');
    }
}


