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
        // 1000000000
        // 10000000
        // 1000000
        // 100000
        // 10000
        // 1000
        // 100
        // 10
        // 1
        String[] roman = new String[]{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int[] value = new int[]{1000000000,900000000,500000000,40000000,100000000,90000000,5000000,4000000,1000000,900000,500000,400000,100000,90000,50000,40000,10000,9000,5000,4000,1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String result = "";
        for (int i = 0; i < value.length; i++) {
            while (number >= value[i]) {
                number = number - value[i];
                result