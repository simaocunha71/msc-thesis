import java.util.*;
import java.lang.*;

class Solution {
    /**
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.
    <p>
    It must be implemented like this:
    >>> sortArray(Arrays.asList(1, 5, 2, 3, 4)).equals(Arrays.asList(1, 2, 3, 4, 5))
    >>> sortArray(Arrays.asList(-2, -3, -4, -5, -6)).equals(Arrays.asList(-6, -5, -4, -3, -2))
    >>> sortArray(Arrays.asList(1, 0, 2, 3, 4)).equals(Arrays.asList(0, 1, 2, 3, 4))
     */
    public List<Integer> sortArray(List<Integer> arr) {
        // Check if the list is empty
        if (arr.isEmpty()) {
            return arr;
        }

        // Create a list to store the binary representations of the numbers
        List<String> binaryArr = new ArrayList<>();
        for (int num : arr) {
            binaryArr.add(Integer.toBinaryString(num));
        }

        // Sort the list based on the number of ones in their binary representation
        binaryArr.sort((a, b) -> {
            int countA = countOnes(a);
            int countB = countOnes(b);
            if (countA == countB) {
                return Integer.compare(Integer.parseInt(a, 2), Integer.parseInt(b, 2));
            }
            return Integer.compare(countA, countB);
        });

        // Convert the binary representations back to decimal values
        List<Integer> sortedArr = new ArrayList<>();
        for (String binary : binaryArr) {
            sortedArr.add(Integer.parseInt(binary, 2));
        }

        return sortedArr;
    }

    // Helper method to count the number of ones in a binary string
    private int countOnes(String binary) {
        int count = 0;
        for (char c : binary.toCharArray()) {
            if (c == '1') {
                count++;
            }
        }
        return count;
    }
}