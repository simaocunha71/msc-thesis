import java.util.*;
import java.lang.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
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
            if ((isNegative && sum > 0) || (!isNegative && sum >= 0)) {
                count++;
            }
        }
        return count;
    }
}