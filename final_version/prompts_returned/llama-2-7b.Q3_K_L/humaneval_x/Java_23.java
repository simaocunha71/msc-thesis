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
        if (string == null || string.length() == 0) return 0;
        
        if (string.charAt(0) == '\r' && string.charAt(1) != '\n')
            return 1 + strlen(string.substring(2));
        
        int length = 1;
        for (int i=0 ; i<string.length() ; ++i){
            if ((string.charAt(i) == '\r' && string.charAt(i+1) != '\n') || (string.charAt(i) == '\n'))
                length++;
        }
        
        return length;
    }
}
