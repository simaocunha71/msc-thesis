import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        // Sort in ascending order
        // based on sum of digits
        // and if there are several items with similar sum of digits,
        // order them based on their index in original list
        Collections.sort(nums, (a, b) -> {
            String sa = Integer.toString(a);
            String sb = Integer.toString(b);
            int sumA = sa.chars().sum();
            int sumB = sb.chars().sum();
            if (sumA == sumB)
                return Integer.compare(a, b);
            return Integer.compare(sumA, sumB);
        });
        return nums;
    }
}

