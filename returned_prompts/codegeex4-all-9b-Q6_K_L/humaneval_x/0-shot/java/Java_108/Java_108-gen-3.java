import java.util.*;
import java.lang.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            if (sumDigits(num) > 0) {
                count++;
            }
        }
        return count;
    }

    private int sumDigits(int num) {
        int sum = 0;
        boolean isNegative = false;
        if (num < 0) {
            num = -num;
            isNegative = true;
        }
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return isNegative ? -sum : sum;
    }
}