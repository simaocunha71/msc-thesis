import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sortNumbers("three one five")
    "one three five"
     */
    public String sortNumbers(String numbers) {
        int[] num = new int[10];
        for(int i = 0; i < numbers.length(); i++) {
            num[i] = Character.getNumericValue(numbers.charAt(i));
        }
        Arrays.sort(num);
        String out = "";
        for(int i = 0; i < num.length; i++) {
            out += num[i];
        }
        return out;
    }
}
