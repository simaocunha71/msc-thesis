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

        if (text == null || text.length() == 0) {
            return text;
        }

        StringBuilder sb = new StringBuilder();

        int count = 0;

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);

            if (c == ' ') {
                if (count < 2) {
                    sb.append('_');
                    count++;
                } else {
                    sb.append("-");
                    count = 0;
                }
            } else {
                sb.append(c);
                count = 0;
            }
        }

        return sb.toString();
    }
}