import java.util.*;
class Solution {
    public int sumSquares(List<Integer> a) {
        int n = a.size();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int num = a.get(i);
            sum += num * num;
        }
        return sum;
    }
}