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
        for (int i=0;i<text.length();i++) { 
            char c = text.charAt(i);
            switch (c) {
                case ' ': sb.append('_'); break; // replace spaces with underscore
                case '-': sb.append('-'); break; // replace - with - if more than two consecutive - 
            }
        }
        return sb.toString();
    }
}