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
        if (text.length() < 3) return text;
        char c = getSpace(text);
        StringBuilder b = new StringBuilder();
        for (char ch : text.toCharArray()) {
            if ((ch == ' ') && (b.length() > 2)) {
                b.append('_');
            } else {
                b.append(ch);
            }
        }
        StringBuffer sb = new StringBuffer();
        for (String s : b.toString().split(" ")) {
            sb.append(s);
        }
        return sb.toString();
    }

    private char getSpace(String text) {
        if (text != null && !"".equals(text)) {
            for (int i = 0; i < text.length(); i++) {
                if (Character.isWhitespace(text.charAt(i))) {
                    return Character.toUpperCase(text.charAt(i));
                }
            }
        }
        return '-';
    }
}