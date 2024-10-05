import java.util.*;
import java.lang.*;

class Solution {
    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10 && isOdd(num) && isOddFirstAndLastDigit(num)) {
                count++;
            }
        }
        return count;
    }

    private boolean isOdd(int num) {
        return num % 2 != 0;
    }

    private boolean isOddFirstAndLastDigit(int num) {
        int firstDigit = Math.abs(num) / 10;
        int lastDigit = Math.abs(num) % 10;
        return isOdd(firstDigit) && isOdd(lastDigit);
    }
}