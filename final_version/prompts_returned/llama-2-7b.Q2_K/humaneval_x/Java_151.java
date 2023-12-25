import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    doubleTheDifference(Arrays.asList(1, 3, 2, 0)) == 1 + 9 + 0 + 0 = 10
    doubleTheDifference(Arrays.asList(-1, -2, 0)) == 0
    doubleTheDifference(Arrays.asList(9, -2)) == 81
    doubleTheDifference(Arrays.asList(0)) == 0

    If the input list is empty, return 0.
     */
    public int doubleTheDifference(List<Object> lst) {
        if (lst == null || lst.size() < 1 ) {
            return Integer.MIN_VALUE;
        }
        List<Double> oddSums = new ArrayList();
        for (int i = 0; i < lst.size(); i++) {
            double val = Double.parseDouble(lst.get(i).toString());
            if ((val != null) && !Double.isInfinite(val)) {
                oddSums.add((double) Math.sqrt(val * (Math.pow(2, 1))) - val);
                oddSums.remove(Double.MIN_VALUE); // Remove Double.MIN_VALUE to avoid division by zero
            }
        }
        if (oddSums.size() == 0) {
            return Integer.MIN_VALUE;
        } else {
            int sum = 0;
            for (double d : oddSums) {
                sum += d; // Sum doubles to integers
            }
            return (int) Math.max(sum, 1);
        }
    }
}
