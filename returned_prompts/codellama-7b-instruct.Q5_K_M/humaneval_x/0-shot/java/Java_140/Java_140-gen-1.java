import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string text, replace all spaces in it with underscores,
    and if a string has more than 2 consecutive spaces,
    then replace all consecutive spaces with -

    fixSpaces("Example") == "Example"
    fixSpaces("Example 1") == "Example_1"
    fixSpaces(" Example 2") == "_Example_2"
    fixSpaces(" Example   3") == "_Example-3"
     */
    public String fixSpaces(String text) {
        String result = "";
        char[] words = text.toCharArray();
        for (int i = 0; i < words.length; i++) {
            if (words[i] != ' ') {
                result += words[i];
            }
            else if (words[i] == ' ' && i == words.length - 1) {
                result += "_";
            }
            else if (words[i] == ' ' && words[i+1] == ' ') {
                result += "-";
            }
            else if (words[i] == ' ' && words[i+1] != ' ') {
                result += "_";
            }
        }
        return result;
    }
}
