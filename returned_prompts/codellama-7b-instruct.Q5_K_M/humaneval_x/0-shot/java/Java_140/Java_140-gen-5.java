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
        String[] words = text.split(" ");
        for (String word : words) {
            if (word.length() > 0) {
                if (word.length() > 2) {
                    result += word.replace(" ", "-");
                } else {
                    result += word.replace(" ", "_");
                }
            }
        }
        return result;
    }
}
