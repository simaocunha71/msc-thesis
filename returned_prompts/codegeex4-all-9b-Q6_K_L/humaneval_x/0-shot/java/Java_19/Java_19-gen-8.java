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
        String[] numArr = numbers.split(" ");
        String[] numArr2 = new String[numArr.length];
        int[] numArr3 = new int[numArr.length];
        int i = 0;
        for(String numStr : numArr) {
            if(numStr.equals("zero")) numArr3[i] = 0;
            if(numStr.equals("one")) numArr3[i] = 1;
            if(numStr.equals("two")) numArr3[i] = 2;
            if(numStr.equals("three")) numArr3[i] = 3;
            if(numStr.equals("four")) numArr3[i] = 4;
            if(numStr.equals("five")) numArr3[i] = 5;
            if(numStr.equals("six")) numArr3[i] = 6;
            if(numStr.equals("seven")) numArr3[i] = 7;
            if(numStr.equals("eight")) numArr3[i] = 8;
            if(numStr.equals("nine")) numArr3[i] = 9;
            i++;
        }
        Arrays.sort(numArr3);
        int j = 0;
        for(int num : numArr3) {
            if(num == 0) numArr2[j] = "zero";
            if(num == 1) numArr2[j] = "one";
            if(num == 2) numArr2[j] = "two";
            if(num == 3) numArr2[j] = "three";
            if(num == 4) numArr2[j] = "four";
            if(num == 5) numArr2[j] = "five";
            if(num == 6) numArr2[j] = "six";
            if(num == 7) numArr2[j] = "seven";
            if(num == 8) numArr2[j] = "eight";
            if(num == 9) numArr2[j