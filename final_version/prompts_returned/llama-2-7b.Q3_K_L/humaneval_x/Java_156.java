import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> intToMiniRoman(19) == "xix"
    >>> intToMiniRoman(152) == "clii"
    >>> intToMiniRoman(426) == "cdxxvi"
     */
    public String intToMiniRoman(int number) {
        // your code here
        String[] symbols = {"M","X", "L", "C",  "D", "I", "V", "X"};
        StringBuilder sb = new StringBuilder();
        
        while (number > 0){
            int reminder = number % 10; //get last digit
            
            if(reminder == 9 || reminder == 8 || reminder == 7){
                sb.append(symbols[3]);
            }
            else if(reminder == 6 || reminder == 5 || reminder == 4){
                sb.append(symbols[2]);
            }else{
                
                sb.append(symbols[1]);
            }
            
            number = number / 10; //get the last digit and divide by 10 to get next int value
            
        }
        return sb.toString();
    }
}