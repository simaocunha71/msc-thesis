```java
import java.util.*;
import java.lang.*;

class Solution {
    public String sortNumbers(String numbers) {
        if (numbers == null || numbers.isEmpty()) {
            return "";
        }
        String[] parts = numbers.split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            nums[i] = numberToInteger(parts[i]);
        }
        Arrays.sort(nums);
        StringBuilder sb = new StringBuilder();
        for (int num : nums) {
            sb.append(integerToNumber(num));
            sb.append(" ");
        }
        return sb.toString().trim();
    }

    private int numberToInteger(String number) {
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

    private String integerToNumber(int number) {
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
                throw new IllegalArgumentException("Invalid number: " + number);
        }
    }
}
```