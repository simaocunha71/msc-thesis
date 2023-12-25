import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parseNestedParens("(()()) ((())) () ((())()())")
    [2, 3, 1, 3]
     */
    public List<Integer> parseNestedParens(String paren_string) {
        //Write your code here
        List<Integer> res=new LinkedList<>();
        String str="";//str is used to track the last match of parenthesis.
        for (int i = 0; i < paren_string.length(); i++) {
            char c=paren_string.charAt(i);
            if (c == '(') {//checking whether current character is a '(' or not.
                str=str+"(";//if its '(' then adding it in list.
                res.add(1);//and incrementing the level of nesting
            } else if (c == ')'){//otherwise checking whether last match was ')' or not.
                str=str.substring(0, str.length()-1);//removing last  character(')') from string.
                res.add(-1);//and decrementing level of nesting.
            } else if (c == ')') { //checking whether current character is a ')' or not.
                str="";//reset the level of nesting to zero by setting its value equal to empty string "".
                res=res.subList(0, res.size()-1);//and removing last match of parenthesis from list.
            } else {//otherwise we are not handling anything else except ')' and '('.
                str+=""+c;//incrementing the level of nesting by one.
                if (str.length()==2){//if string length is equal to 2 then res.add(0);//adding a zero at index[1].
                    res=res.subList(0, res.size()