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
        // Write your code here
        return nums.stream().sorted((a, b) -> {
            String sa = String.valueOf(a);
            String sb = String.valueOf(b);
            int suma = 0;
            int sumb = 0;
            for (int i = 0; i < sa.length(); i++) {
                suma += sa.charAt(i) - '0';
            }
            for (int j = 0; j < sb.length(); j++) {
                sumb += sb.charAt(j) - '0';
            }
            if (suma != sumb) {
                return suma - sumb;
            } else {
                return a - b;
            }
        }).collect(Collectors.toList());
    }
}

//-----------------------------------------------------------------------------

