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
        if (nums.size() == 0)
            return nums;
        nums.sort((a, b) -> {
            if (sumDigits(a) == sumDigits(b))
                return Integer.compare(nums.indexOf(a), nums.indexOf(b));
            return Integer.compare(sumDigits(a), sumDigits(b));
        });
        return nums;
    }

    private int sumDigits(int x) {
        if (x == 0)
            return 0;
        return 1 + sumDigits(x / 10);
    }
}

