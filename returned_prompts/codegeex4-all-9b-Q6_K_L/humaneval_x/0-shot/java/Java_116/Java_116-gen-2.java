import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        // Sort the array based on the number of ones in their binary representation
        arr.sort((a, b) -> {
            int countA = Integer.bitCount(a);
            int countB = Integer.bitCount(b);
            if (countA == countB) {
                return Integer.compare(a, b);
            } else {
                return Integer.compare(countA, countB);
            }
        });
        return arr;
    }
}