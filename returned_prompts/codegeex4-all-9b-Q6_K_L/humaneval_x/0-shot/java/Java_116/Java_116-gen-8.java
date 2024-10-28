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
        return arr.stream()
                .sorted((a, b) -> {
                    int countA = Integer.bitCount(a);
                    int countB = Integer.bitCount(b);
                    if (countA != countB) {
                        return Integer.compare(countA, countB);
                    } else {
                        return Integer.compare(a, b);
                    }
                })
                .collect(Collectors.toList());
    }
}