import java.util.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        List<Integer> list = new ArrayList<>();
        int count = 0;
        while (num > 0) {
            if (num % 2 == 0) {
                count++;
            }
            num /= 10;
        }
        list.add(count);
        count = 0;
        while (num > 0) {
            if (num % 2 == 1) {
                count++;
            }
            num /= 10;
        }
        list.add(count);
        return list;
    }
}
