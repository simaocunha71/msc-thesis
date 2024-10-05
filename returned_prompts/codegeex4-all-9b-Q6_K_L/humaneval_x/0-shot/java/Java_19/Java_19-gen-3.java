import java.util.*;
import java.lang.*;

class Solution {
    public String sortNumbers(String numbers) {
        String[] nums = numbers.split(" ");
        Arrays.sort(nums, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return Integer.compare(getNumber(s1), getNumber(s2));
            }
        });
        return String.join(" ", nums);
    }

    private int getNumber(String number) {
        switch (number) {
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
                throw new IllegalArgumentException("Invalid number: " + number);
        }
    }
}