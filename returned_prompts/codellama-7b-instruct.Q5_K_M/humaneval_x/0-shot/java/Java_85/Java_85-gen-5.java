import java.util.*;

class Solution {
    public int add(List<Integer> lst) {
        int sum = 0;
        for (int i = 1; i < lst.size(); i += 2) {
            sum += lst.get(i);
        }
        return sum;
    }
}
