import java.util.*;
import java.lang.*;
class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double num : lst) {
            int upper = (int) Math.ceil(num);
            sum += upper * upper;
        }
        return sum;
    }
}
