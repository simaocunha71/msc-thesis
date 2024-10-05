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
        for(int i=0; i<string.length(); i++){
            if(Character.isUpperCase(string.charAt(i))){
                result += Character.toLowerCase(string.charAt(i));
            }
            else {
                result += Character.toUpperCase(string.charAt(i));
            }
        }
        return result;
    }
}