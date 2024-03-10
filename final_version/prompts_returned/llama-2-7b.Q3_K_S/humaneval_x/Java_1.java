import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separateParenGroups("( ) (( )) (( )( ))")
    ["()", "(())", "(()())"]
     */
    public List<String> separateParenGroups(String paren_string) {
        List<String> groups = new ArrayList<>();
        if (paren_string == null) return groups;
        
        for(int i=0 ; i < paren_string.length() ;i++) {
            char ch = paren_string.charAt(i);
            
            // If this is not a brace, then add it to the string and continue searching.
            if (ch == '(' || ch == '{' || ch == '<') groups.add(String.valueOf((int)ch));
            else {
                StringBuffer paren_group = new StringBuffer();
                
                // If this is a brace, then search for any closing brackets within the group and add them to it.
                if (i < paren_string.length() - 1 && ch == ')' || ch == '}' || ch == '>') {
                    while(i+1 <= paren_string.length()) {
                        char next = paren_string.charAt(++i);
                        
                        // If the next is not a brace, then remove it from the string and continue searching.
                        if (next != ')' && next != '}') i--; 
                            
                        // If the next is an open bracket of the same kind that we are looking for - add it to our group.
                        else {
                            paren_group.append((int) next);
                            
                            // If this is a closing brace, then do not add this to the group since it indicates that the group is closed.
                            if (ch == ')' || ch == '}