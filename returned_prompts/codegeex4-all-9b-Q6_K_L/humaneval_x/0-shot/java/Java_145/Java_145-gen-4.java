import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> orderByPoints(Arrays.asList(1, 11, -1, -11, -12)) == [-1, -11, 1, -12, 11]
    >>> orderByPoints(Arrays.asList()) == []
     */
    public List<Integer> orderByPoints(List<Integer> nums) {
        List<Integer> result = new ArrayList<>(nums);
        result.sort(Comparator.comparingInt(num -> sumDigits(num)));
        return result;
    }

    private int sumDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += Math.abs(num % 10);
            num /= 10;
        }
        return sum;
    }
}