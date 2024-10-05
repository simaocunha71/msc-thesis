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

        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                result += "_";
            } else {
                result += text.charAt(i);
            }
        }

        return result;
    }

    public String fixSpaces2(String text) {

        String result = "";
        int count = 0;

        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                count++;
            } else {
                if (count > 2) {
                    result += "-";
                    count = 0;
                }
                result += text.charAt(i);
            }
        }

        return result;
    }
}
