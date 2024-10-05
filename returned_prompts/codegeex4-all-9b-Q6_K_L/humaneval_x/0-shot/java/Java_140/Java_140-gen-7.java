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
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                count++;
                if (count == 1) {
                    sb.append('_');
                } else if (count > 2) {
                    sb.append('-');
                }
            } else {
                sb.append(c);
                count = 0;
            }
        }
        return sb.toString();
    }
}