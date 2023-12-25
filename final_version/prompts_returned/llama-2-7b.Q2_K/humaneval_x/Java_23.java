import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return length of given string
    >>> strlen("")
    0
    >>> strlen("abc")
    3
     */
    public int strlen(String string) {
        if (string == null || string.length() == 0) {
            return 0;
        }
        final StringBuilder sb = new StringBuilder();
        for (int i=0;i<string.length();i++){
           char c = string.charAt(i);
           sb.append(c).append(' ');
        }
        sb.setLength(sb.length()-1); // remove the last character if any
        return sb.length();
    }
}