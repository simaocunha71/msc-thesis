import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generateIntegers(2, 8) => [2, 4, 6, 8]
    generateIntegers(8, 2) => [2, 4, 6, 8]
    generateIntegers(10, 14) => []
     */
    public List<Integer> generateIntegers(int a, int b) {
        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.generateIntegers(2, 8)); // [2, 4, 6, 8]
        System.out.println(solution.generateIntegers(8, 2)); // [2, 4, 6, 8]
        System.out.println(solution.generateIntegers(10, 14)); // []
    }
}