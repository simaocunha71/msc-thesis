import java.util.*;
import java.lang.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double d : lst) {
            sum += (int)Math.ceil(d) * (int)Math.ceil(d);
        }
        return sum;
    }
}