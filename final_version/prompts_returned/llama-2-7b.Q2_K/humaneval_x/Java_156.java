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
        if (number <= 0 || number > 1000) return null; // check all restrictions are satisfied
        
        if (number % 10 > 9 && number % 5 > 4) return "l" + intToMiniRoman(number / 10);
        else if (number % 10 > 8) return "xl" + intToMiniRoman((number - 2) / 10);
        
        else { // do all other cases
            String str = "";
            int lastDigit = number % 10;
            if (lastDigit >= 5 && lastDigit <= 9)
                str += 'm';
            else if (lastDigit == 4 || lastDigit > 9)
                str += 'iv';
            else if (lastDigit == 3 || lastDigit > 8 )
                str += 'x';
            else if (lastDigit >= 2 && lastDigit <= 7) // 01, 02 etc.
                str += 'i' + 'i';
            else
                str += intToMiniRoman(number - ((number / 10) * 9)); // (lastDigit + "lxvi")
            
            System.out.println("str = "+str);
            return str;
        }
        
    }
}