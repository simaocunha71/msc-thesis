import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flipCase("Hello")
    "hELLO"
     */
    public String flipCase(String string) {
        StringBuilder builder = new StringBuilder();
        for (int i=0;i<string.length();i++)
            {
                char c = string.charAt(i);
                if ((c=='e')||(c=='E')){
                    c='3';
                }else if((c=='l')||(c=='L')){
                    c='1';
                } else if((c=='a')||(c=='A')) {
                    c='4';
                }
                builder.append(c);
            }
        return builder.toString();
     }
}