        String[] symbol = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int[] value = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        StringBuilder roman = new StringBuilder();

        for(int i = 0; i < value.length && number > 0; i++) {
            while(value[i] <= number) {
                number -= value[i];
                roman.append(symbol[i]);
            }
        }

        return roman.toString();
    }
}

This program converts an integer to its equivalent Roman numeral. The integer should be between 1 and 1000 inclusive. It uses a while loop to subtract the value of the Roman symbol from the number while the value is less than or equal to the number. The symbol is then appended to the StringBuilder. The loop continues until the number becomes zero. Finally, the string is returned.

It's important to note that this program only works for numbers between 1 and 1000. If you need to convert numbers outside of this range, you would need to adjust the value and symbol arrays accordingly.
*/

// Solution ends here

// Test cases start here

import org.junit.*;
import static org.junit.Assert.*;

public class TestSolution {
    @Test
    public void testIntToMiniRoman() {
        Solution sol = new Solution();
        assertEquals("xix", sol.intToMiniRoman(19));
        assertEquals("clii", sol.intToMiniRoman(152));
        assertEquals("cdxxvi", sol.intToMiniRoman(426));
    }
}

// Test cases end here

// Code ends here

// The code starts here

import java.util.*;
import java.lang.*;

class Solution  {
    public String intToMiniRoman(int num)  {
        String[] symbol = {"M","CM","D","CD","C","XC","L","X