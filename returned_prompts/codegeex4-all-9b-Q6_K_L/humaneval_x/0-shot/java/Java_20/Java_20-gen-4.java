import java.util.*;
import java.lang.*;

class Solution {
    public List<Double> findClosestElements(List<Double> numbers) {
        Collections.sort(numbers);
        List<Double> result = new ArrayList<>();
        double minDiff = Double.MAX_VALUE;
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < minDiff) {
                minDiff = diff;
                result.clear();
                result.add(numbers.get(i));
                result.add(numbers.get(i + 1));
            } else if (diff == minDiff) {
                result.add(numbers.get(i));
                result.add(numbers.get(i + 1));
            }
        }
        return result;
    }
}