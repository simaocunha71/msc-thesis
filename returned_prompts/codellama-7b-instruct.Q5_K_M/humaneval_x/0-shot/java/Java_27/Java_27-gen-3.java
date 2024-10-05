import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flipCase("Hello")
    "hELLO"
     */
    public String flipCase(String string) {

        for (int i = 0; i < string.length(); i++) {
            if (Character.isLowerCase(string.charAt(i))) {
                string = string.substring(0, i) + Character.toUpperCase(string.charAt(i)) + string.substring(i + 1);
            } else if (Character.isUpperCase(string.charAt(i))) {
                string = string.substring(0, i) + Character.toLowerCase(string.charAt(i)) + string.substring(i + 1);
            }
        }

        return string;
    }
}
