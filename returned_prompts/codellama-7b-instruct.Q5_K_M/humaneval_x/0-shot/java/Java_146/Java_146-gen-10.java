import java.util.*;

class Solution {
    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10 && (num % 10 == 1 || num % 10 == 3 || num % 10 == 5 || num % 10 == 7 || num % 10 == 9)) {
                count++;
            }
        }
        return count;
    }
}

