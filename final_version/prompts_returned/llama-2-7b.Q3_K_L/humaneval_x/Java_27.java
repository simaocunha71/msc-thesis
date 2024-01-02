import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flipCase("Hello")
    "hELLO"
     */
    public String flipCase(String string) {
        char[] c = string.toCharArray();
        for (int i=0; i<c.length ;i++){
            if (Character.isLetter(c[i])){ // lower case
                c[i]-='a';
            } else if (Character.isUpperCase(c[i])) { // upper case
                c[i]+=32; 
            }
        }        
        return new String(c);
    }  
}