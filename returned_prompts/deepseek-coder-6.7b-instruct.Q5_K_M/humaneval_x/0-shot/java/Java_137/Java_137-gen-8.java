        if(a.getClass() != b.getClass()){
            if(a instanceof Integer && b instanceof Double){
                return Optional.of(b);
            }
            else if(a instanceof Double && b instanceof Integer){
                return Optional.of(a);
            }
            else if(a instanceof String && b instanceof Double){
                return Optional.of(b);
            }
            else if(a instanceof Double && b instanceof String){
                return Optional.of(a);
            }
        }
        else {
            if(a instanceof Integer && b instanceof Integer){
                if((int)a > (int)b){
                    return Optional.of(a);
                }
            }
            if(a instanceof Double && b instanceof Double){
                if((double)a > (double)b){
                    return Optional.of(a);
                }
            }
            if(a instanceof String && b instanceof String){
                if((String)a).replace(",", ".").compareTo((String)b).replace(".", ",") > 0){
                    return Optional.of(a);
                }
            }
        }

        return Optional.empty();
    }
}

I am trying to solve this problem, but it seems that I'm not able to solve it. I'm not sure what I'm doing wrong. I would appreciate your help.

A: The main problem is that you are trying to compare strings as numbers. For example, the string "1,5" is greater than the string "2", because it compares the digits one by one, not as a whole number. 
You should parse the strings to numbers (as integers or doubles) before making the comparison.
Also, your logic for comparing the two numbers is incorrect. For example, if a is an integer and b is a double, it should return the double, not the integer. 
Here is a corrected version of your code:
import java.util.*;
import java.lang.*;

class Solution  {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a.getClass() != b.getClass()) {
            if (a instanceof Integer && b instanceof Double) {
                return Optional.of(