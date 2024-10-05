import java.util.*;
import java.lang.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double d : lst) {
            sum += Math.ceil(d) * Math.ceil(d);
        }
        return sum;
    }
}