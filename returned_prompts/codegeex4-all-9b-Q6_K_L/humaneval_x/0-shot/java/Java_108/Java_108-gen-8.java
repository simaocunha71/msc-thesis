import java.util.*;
import java.lang.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            if (num > 0) {
                count++;
            } else {
                int sum = 0;
                while (num != 0) {
                    sum += Math.abs(num % 10);
                    num /= 10;
                }
                if (sum > 0) {
                    count++;
                }
            }
        }
        return count;
    }
}