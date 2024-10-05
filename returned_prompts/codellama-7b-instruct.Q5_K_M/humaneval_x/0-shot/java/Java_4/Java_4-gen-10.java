import java.util.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        // Write your solution here
        double mean = 0.0;
        for (Double number : numbers) {
            mean += number;
        }
        mean /= numbers.size();

        double mad = 0.0;
        for (Double number : numbers) {
            mad += Math.abs(number - mean);
        }
        mad /= numbers.size();

        return mad;
    }
}
