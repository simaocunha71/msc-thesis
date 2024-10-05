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
        String[] strArray = numbers.split(" ");
        int[] numArray = new int[strArray.length];
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int temp;

        for (int i = 0; i < strArray.length; i++) {
            numArray[i] = Integer.parseInt(strArray[i]);
            if (numArray[i] < min) {
                min = numArray[i];
            }
            if (numArray[i] > max) {
                max = numArray[i];
            }
        }

        String[] sorted = new String[strArray.length];
        for (int i = min; i <= max; i++) {
            for (int j = 0; j < strArray.length; j++) {
                if (numArray[j] == i) {
                    temp = numArray[j];
                    numArray[j] = numArray[i];
                    numArray[i] = temp;
                    sorted[i] = String.valueOf(numArray[i]);
                    break;
                }
            }
        }

        for (int i = 0; i < sorted.length; i++) {
            if (sorted[i] != null) {
                System.out.print(sorted[i] + " ");
            }
        }
        return null;
    }
}
