import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        // number of carrots eaten after meals
        int eaten = number + need;
        // number of carrots left after meals
        int left = Math.max(0, remaining - need);
        return Arrays.asList(eaten, left);
    }
}