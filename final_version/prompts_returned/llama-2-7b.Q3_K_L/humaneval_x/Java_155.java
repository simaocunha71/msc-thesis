import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an integer. return a tuple that has the number of even and odd digits respectively.
    
     Example:
        evenOddCount(-12) ==> (1, 1)
        evenOddCount(123) ==> (1, 2)
     */
    public List<Integer> evenOddCount(int num) {
        
        ArrayList<Integer> result = new ArrayList<>();
        String digits = "";
        while (num > 0){
            digits += Character.valueOf((char)(num % 10 + '0'));
            num /= 10;
        }
        if(digits.length() == 1) {
           result.add(1);
         return result;
         } else {
             int even = 0, odd = 0;
            for (int i = 0; i < digits.length();i++){
                if(Character.valueOf((char)(digits.charAt(i))).equals('2')){
                    even++;
                } else {
                    odd++;
                }
            }
         return result;
        }
    }
}