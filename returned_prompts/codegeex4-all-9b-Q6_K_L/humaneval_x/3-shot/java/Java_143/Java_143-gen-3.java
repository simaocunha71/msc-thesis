
The problem with the first code is that you are comparing all elements with each other. That will take O(n^2) time which is bad. You can improve this code by sorting the array and then iterating through it once. That will take O(n log n) time which is much better. Also, you can use a HashSet to check if an element has been seen before. That will take O(1) time for each check.
Here is the improved code:
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
        Set<Double> seen = new HashSet<>();
        for (double number : numbers) {
            if (seen.contains(number - threshold) || seen.contains(number + threshold)) {
                return true;
            }
            seen.add(number);
        }
        return false;
    }
}

The problem with the second code is that you are using StringBuilder to build the string. That is unnecessary. You can use a simple string to build the string. Also, you are using a StringBuilder to build the current string. That is unnecessary. You can use a simple string to build the current string. Also, you are using a StringBuilder to build the result string. That is unnecessary. You can use a simple string to build the result string.
Here is the improved code