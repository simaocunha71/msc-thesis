import java.util.*;
import java.lang.*;

class Solution {
    /**
    Your task is to implement a function that will simplify the expression
    x * n. The function returns true if x * n evaluates to a whole number and false
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = true
    simplify("1/6", "2/1") = false
    simplify("7/10", "10/2") = false
     */
    public boolean simplify(String x, String n) {
        // your code goes here
        int a=0,b=0,c=0,d=0;
        a=x.indexOf("/");
        b=n.indexOf("/");
        c=Integer.parseInt(x.substring(0,a));
        d=Integer.parseInt(n.substring(0,b));
        int e=Integer.parseInt(x.substring(a+1,x.length()));
        int f=Integer.parseInt(n.substring(b+1,n.length()));
        int g=c*d;
        int h=e*f;
        if(g==h)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
