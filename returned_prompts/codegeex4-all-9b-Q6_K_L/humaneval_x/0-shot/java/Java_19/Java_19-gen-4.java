```java
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
        Integer[] numArrInt = new Integer[numArr.length];
        for (int i = 0; i < numArr.length; i++) {
            numArrInt[i] = convertNumeralToInt(numArr[i]);
        }
        Arrays.sort(numArrInt);
        StringBuilder sortedNums = new StringBuilder();
        for (int i = 0; i < numArrInt.length; i++) {
            sortedNums.append(convertIntToNumeral(numArrInt[i]));
            if (i < numArrInt.length - 1) {
                sortedNums.append(" ");
            }
        }
        return sortedNums.toString();
    }

    private Integer convertNumeralToInt(String numeral) {
        switch (numeral) {
            case "zero":
                return 0;
            case "one":
                return 1;
            case "two":
                return 2;
            case "three":
                return 3;
            case "four":
                return 4;
            case "five":
                return 5;
            case "six":
                return 6;
            case "seven":
                return 7;
            case "eight":
                return 8;
            case "nine":
                return 9;
            default:
                throw new IllegalArgumentException("Invalid numeral: " + numeral);
        }
    }

    private String convertIntToNumeral(int number) {
        switch (number) {
            case 0:
                return "zero";
            case 1:
                return "one";
            case 2:
                return "two";
            case 3:
                return "three";
            case 4:
                return "four";
            case 5:
                return "five";
            case 6:
                return "six";
            case 7:
                return "seven";
            case 8:
                return "eight";
            case 9:
                return "nine";
            default:
                throw new IllegalArgumentException