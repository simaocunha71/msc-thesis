import java.util.*;

class Solution {
    public static List<Double> rescaleToUnit(List<Double> numbers) {
        // Find the min and max values in the list
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        // Create a list to hold the rescaled values
        List<Double> rescaled = new ArrayList<>();
        // Loop through each number and rescale it
        for (double number : numbers) {
            rescaled.add((number - min) / (max - min));
        }
        return rescaled;
    }
}
