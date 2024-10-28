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

        int spaces = 0;
        int consecutiveSpaces = 0;
        StringBuffer result = new StringBuffer();
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                spaces++;
            } else if (c != ' ' && spaces > 0) {
                for (int i = 0; i < spaces; i++) {
                    result.append('_');
                }
                spaces = 0;
            }
            result.append(c);
            if (c == ' ') {
                consecutiveSpaces++;
            } else {
                consecutiveSpaces = 0;
            }
            if (consecutiveSpaces >= 3) {
                result.append('-');
                consecutiveSpaces = 0;
            }
        }
        return result.toString();
    }
}