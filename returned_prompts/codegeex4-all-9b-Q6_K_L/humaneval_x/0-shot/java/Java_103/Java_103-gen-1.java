import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m) {
            return -1;
        }
        double avg = 0.0;
        for (int i = n; i <= m; i++) {
            avg += i;
        }
        avg = Math.round(avg / (m - n + 1));
        return Integer.toBinaryString((int) avg);
    }
}

class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.roundedAvg(1, 5)); // "11"
        System.out.println(s.roundedAvg(7, 5)); // -1
        System.out.println(s.roundedAvg(10, 20)); // "1111"
        System.out.println(s.roundedAvg(20, 33)); // "11011"
    }
}