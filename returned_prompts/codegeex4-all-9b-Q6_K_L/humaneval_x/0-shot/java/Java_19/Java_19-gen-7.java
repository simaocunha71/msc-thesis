import java.util.*;
import java.lang.*;

class Solution {
    public String sortNumbers(String numbers) {
        String[] numWords = numbers.split(" ");
        int[] numVals = new int[numWords.length];
        for (int i = 0; i < numWords.length; i++) {
            numVals[i] = numberToValue(numWords[i]);
        }
        Arrays.sort(numVals);
        String result = "";
        for (int i = 0; i < numVals.length; i++) {
            result += valueToNumber(numVals[i]) + " ";
        }
        return result.trim();
    }
    
    private int numberToValue(String word) {
        switch (word) {
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
                throw new IllegalArgumentException("Invalid number word: " + word);
        }
    }
    
    private String valueToNumber(int value) {
        switch (value) {
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
                throw new IllegalArgumentException("Invalid number value: " + value);
        }
    }
}