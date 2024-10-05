import java.util.*;

class Solution {
    public List<Integer> f(int n) {
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(i);
            } else {
                int sum = 0;
                for (int j = 1; j <= i; j++) {
                    sum += j;
                }
                result.add(sum);
            }
        }
        return result;
    }
}
