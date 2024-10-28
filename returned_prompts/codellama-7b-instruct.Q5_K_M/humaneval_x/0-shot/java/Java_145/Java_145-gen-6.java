import java.util.*;

class Solution {
    public int[] orderByPoints(int[] nums) {
        Arrays.sort(nums, (a, b) -> a == b ? 0 : a < b ? -1 : 1);
        return nums;
    }
}
