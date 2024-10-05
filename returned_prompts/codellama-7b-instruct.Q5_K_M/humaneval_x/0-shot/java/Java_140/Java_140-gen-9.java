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

        StringBuffer sb = new StringBuffer(text);
        for (int i = 0; i < sb.length(); i++) {
            if (sb.charAt(i) == ' ') {
                if (i == sb.length() - 1) {
                    sb.append('_');
                } else if (sb.charAt(i + 1) == ' ') {
                    sb.insert(i++, '-');
                } else {
                    sb.insert(i, '_');
                }
            }
        }
        return sb.toString();
    }
}
