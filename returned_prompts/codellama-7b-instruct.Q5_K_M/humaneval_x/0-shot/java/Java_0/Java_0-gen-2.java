import java.util.*;
import java.lang.*;

class Solution {
    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
     */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        // Sort the list
        Collections.sort(numbers);

        // Iterate over the list and check if there are any close pairs
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff1 = numbers.get(i) - numbers.get(i + 1);
            if (diff1 < 0) {
                diff1 = -diff1;
            }

            for (int j = i + 1; j < numbers.size() - 1; j++) {
                double diff2 = numbers.get(j) - numbers.get(j + 1);
                if (diff2 < 0) {
                    diff2 = -diff2;
                }

                if (diff1 + diff2 < threshold) {
                    return true;
                }
            }
        }

        return false;
    }
}


