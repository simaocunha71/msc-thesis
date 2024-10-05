import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        Collections.sort(nums, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int sum1 = sumDigits(o1);
                int sum2 = sumDigits(o2);
                if (sum1 != sum2) {
                    return sum1 - sum2;
                } else {
                    return nums.indexOf(o1) - nums.indexOf(o2);
                }
            }
        });
        return nums;
    }

    private int sumDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}