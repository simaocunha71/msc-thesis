import java.util.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        List<Integer> res = new ArrayList<>();
        int cnt = 0;
        while (num != 0) {
            int digit = num % 10;
            if (digit % 2 == 0) cnt++;
            num /= 10;
        }
        res.add(cnt);
        cnt = 0;
        while (num != 0) {
            int digit = num % 10;
            if (digit % 2 != 0) cnt++;
            num /= 10;
        }
        res.add(cnt);
        return res;
    }
}
