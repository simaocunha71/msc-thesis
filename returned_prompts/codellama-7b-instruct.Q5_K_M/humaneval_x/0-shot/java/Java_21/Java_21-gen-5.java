import java.util.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        List<Double> result = new ArrayList<Double>();
        for (double number : numbers) {
            result.add((number - min) / (max - min));
        }
        return result;
    }
}
