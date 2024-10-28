import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        // Convert each number to its binary representation and count the number of ones
        Map<Integer, Integer> countOnes = new HashMap<>();
        for (int num : arr) {
            String binary = Integer.toBinaryString(num);
            int ones = (int) binary.chars().filter(c -> c == '1').count();
            countOnes.put(num, ones);
        }

        // Sort the array based on the number of ones, then by the decimal value
        arr.sort((a, b) -> {
            int onesA = countOnes.get(a);
            int onesB = countOnes.get(b);
            if (onesA != onesB) {
                return Integer.compare(onesA, onesB);
            } else {
                return Integer.compare(a, b);
            }
        });

        return arr;
    }
}