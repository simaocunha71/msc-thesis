import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        // Write your solution here
        // Sorting a list of integers based on the sum of their digits.
        //
        // Given a list of integers, return a list of integers sorted in
        // ascending order according to the sum of their digits.
        // If there are several items with similar sum of their digits,
        // order them based on their index in the original list.
        //
        // For example,
        // orderByPoints(Arrays.asList(1, 11, -1, -11, -12))
        //   == Arrays.asList(-1, -11, 1, -12, 11)
        //
        // and
        // orderByPoints(Arrays.asList()) == Arrays.asList()
        //
        // Hint:
        //   1. You can use the following formula to get the sum of the
        //      digits of an integer:
        //
        //        sum = (n % 10) + (n / 10)
        //
        //   2. If n is a negative number,
        //      you should consider the absolute value of n.
        //
        //   3. If n is 0, the sum is 0.
        //
        //   4. If n is a positive number,
        //      you can get the absolute value of n by n.
        //
        //   5. If you want to compare two integers,
        //      you can use (n1 - n2) to get the difference between them.
        //
        //   6. If you want to compare two floating-point numbers,
        //      you can use (n1 - n2) to get the difference between them.
        //
        //   7. If you want to compare two strings,
        //      you can use (s1.compareTo(s2)) to get the result.
        //
        //   8. If you want to compare two arrays,
        //      you can use Arrays.equals(arr1, arr2) to get the result.
        //
