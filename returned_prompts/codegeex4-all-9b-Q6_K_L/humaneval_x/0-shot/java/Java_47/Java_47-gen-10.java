import java.util.*;
import java.lang.*;

class Solution {
    public double median(List<Integer> l) {
        // Sort the list in ascending order
        Collections.sort(l);

        // Calculate the median
        int size = l.size();
        if (size % 2 == 0) {
            // If the list size is even, return the average of the two middle elements
            return (l.get(size / 2 - 1) + l.get(size / 2)) / 2.0;
        } else {
            // If the list size is odd, return the middle element
            return l.get(size / 2);
        }
    }
}