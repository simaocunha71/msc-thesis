    import java.util.*;

class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        if (numbers.size() < 2) {
            throw new RuntimeException("List must have at least two elements");
        }

        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> result = new ArrayList<>();
        for (Double num : numbers) {
            result.add((num - min) / (max - min));
        }

        return result;
    }
}A
