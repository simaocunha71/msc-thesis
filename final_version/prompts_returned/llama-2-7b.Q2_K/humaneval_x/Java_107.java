import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
     */
    public List<Integer> evenOddPalindrome(int n) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[][] mapEvenNums = new int[n + 1][]; // [0, n).
        for (int i = 1; i <= n; i++) {
            if (!map.containsKey(i)) {
                map.put(i, 0);
                mapEvenNums[i] = new int[4];
                mapEvenNums[i][2] = 0; // even
                mapEvenNums[i][3] = 0; // odd
            } else {
                int temp;
                if (map.get(i) > 0)
                    mapEvenNums[i][1 - map.get(i)]++; // even
                if (map.get(i) + 2 > n)
                    mapEvenNums[i][4]++; // odd
                else {
                    temp = map.get(i);
                    mapEvenNums[i][1 - map.get(i)]--;// even
                    map