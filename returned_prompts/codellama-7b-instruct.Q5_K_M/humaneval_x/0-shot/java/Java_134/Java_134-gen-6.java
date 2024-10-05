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

        //check if last char is alphabetical
        boolean isLastCharAlphabetic = false;
        int txtLength = txt.length();
        char lastChar = txt.charAt(txtLength - 1);
        if (Character.isAlphabetic(lastChar)) {
            isLastCharAlphabetic = true;
        }

        //check if last char is part of a word
        boolean isLastCharPartOfAWord = false;
        txt = txt.trim(); //remove any leading or trailing spaces
        if (!txt.isEmpty()) {
            txtLength = txt.length();
            lastChar = txt.charAt(txtLength - 1);
            if (lastChar != ' ') {
                String[] words = txt.split(" ");
                String lastWord = words[words.length - 1];
                if (lastWord.length() == 1) {
                    isLastCharPartOfAWord = true;
                }
            }
        }

        return isLastCharAlphabetic && !isLastCharPartOfAWord;
    }
}
