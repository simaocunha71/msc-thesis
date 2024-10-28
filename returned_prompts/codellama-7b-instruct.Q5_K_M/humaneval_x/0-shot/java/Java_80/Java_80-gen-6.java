import java.util.*;
import java.lang.*;

class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        for (int i = 0; i < height.length; i++) {
            for (int j = i + 1; j < height.length; j++) {
                int min = Math.min(height[i], height[j]);
                int diff = Math.abs(height[i] - height[j]);
                max = Math.max(max, min * diff);
            }
        }
        return max;
    }
}



