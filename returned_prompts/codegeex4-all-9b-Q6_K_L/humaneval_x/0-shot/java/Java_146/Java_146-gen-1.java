import java.util.*;
import java.lang.*;

class Solution {
    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10 && isOdd(num)) {
                int lastDigit = num % 10;
                int firstDigit = num;
                while (firstDigit >= 10) {
                    firstDigit /= 10;
                }
                if (isOdd(firstDigit) && isOdd(lastDigit)) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isOdd(int num) {
        return num % 2 != 0;
    }
}