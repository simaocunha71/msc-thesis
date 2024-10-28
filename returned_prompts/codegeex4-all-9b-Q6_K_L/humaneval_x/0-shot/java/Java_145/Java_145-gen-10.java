import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        Collections.sort(nums, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int sumA = sumDigits(a);
                int sumB = sumDigits(b);
                if (sumA == sumB) {
                    return nums.indexOf(a) - nums.indexOf(b);
                } else {
                    return sumA - sumB;
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