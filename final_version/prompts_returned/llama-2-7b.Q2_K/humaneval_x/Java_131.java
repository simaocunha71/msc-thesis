import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
     */
    public int digits(int n) {
        //Write your own code as per the question guidelines.
       if((n % 2)==0){ return 0;}else{String str = String.valueOf(n);StringBuilder sb=new StringBuilder();for(int i=0;i<str.length();i++){if(Character.isDigit(str.charAt(i))||sb.length()>40){sb.append(str.charAt(i));}else{sb.append("0").append(str.charAt(i));}}return Integer.parseInt(sb.toString());
    }
  // main function to test the above code
    public static void main(String[] args) {
        Solution s=new Solution();
            System.out.println("n="+s.digits(12345));
           System.out.println("n="+s.digits(67890));
           System.out.println("n="+s.digits(-67541));
    }
}