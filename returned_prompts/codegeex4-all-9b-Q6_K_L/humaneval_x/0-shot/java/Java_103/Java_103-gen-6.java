import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m) {
            return -1;
        }
        int sum = 0;
        int count = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
            count++;
        }
        int avg = (int) Math.round((double) sum / count);
        return Integer.toBinaryString(avg);
    }
}