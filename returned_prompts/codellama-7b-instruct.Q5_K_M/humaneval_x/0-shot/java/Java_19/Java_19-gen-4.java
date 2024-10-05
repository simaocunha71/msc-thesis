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
        String[] numArray = numbers.split(" ");
        int[] nums = new int[numArray.length];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(numArray[i]);
        }
        Arrays.sort(nums);
        String result = "";
        for (int j = 0; j < nums.length; j++) {
            result += (nums[j] + " ");
        }
        return result.trim();
    }
}
