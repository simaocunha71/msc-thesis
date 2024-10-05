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
        // Write your code here
        String [] number = numbers.split(" ");
        Arrays.sort(number);
        String result = "";
        for(int i = 0; i < number.length; i++)
            result = result + number[i] + " ";
        return result;
    }
}
