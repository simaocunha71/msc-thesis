import java.util.*;
import java.lang.*;

class Solution {
    /**
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> findClosestElements(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 2.2))
    [2.0, 2.2]
    >>> findClosestElements(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 2.0))
    [2.0, 2.0]
     */
    public List<Double> findClosestElements(List<Double> numbers) {
        if (numbers == null || numbers.size() < 2) {
            return null;
        }

        // sort the list
        Collections.sort(numbers);

        // get the smallest and largest numbers
        double smallest = numbers.get(0);
        double largest = numbers.get(numbers.size() - 1);

        // now find the first number that is larger than the smallest
        // and the first number that is smaller than the largest
        int smallestIndex = -1;
        int largestIndex = -1;
        for (int i = 0; i < numbers.size(); i++) {
            double number = numbers.get(i);
            if (number > smallest) {
                smallestIndex = i;
                break;
            }
        }

        for (int i = numbers.size() - 1; i >= 0; i--) {
            double number = numbers.get(i);
            if (number < largest) {
                largestIndex = i;
                break;
            }
        }

        if (smallestIndex == -1 || largestIndex == -1) {
            return null;
        }

        // now find the two numbers that are the closest to each other
        double smallestDifference = Double.MAX_VALUE;
        int closest1Index = -1;
        int closest2Index = -