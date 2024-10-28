import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flipCase("Hello")
    "hELLO"
     */
    public String flipCase(String string) {

        String result = "";

        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) >= 'a' && string.charAt(i) <= 'z') {
                result = result + (char) (string.charAt(i) - 32);
            } else {
                result = result + (char) (string.charAt(i) + 32);
            }
        }

        return result;
    }
}