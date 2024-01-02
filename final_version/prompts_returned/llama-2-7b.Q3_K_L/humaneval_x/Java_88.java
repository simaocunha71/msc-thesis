import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sortArray(Arrays.asList()) => []
    * sortArray(Arrays.asList(5)) => [5]
    * sortArray(Arrays.asList(2, 4, 3, 0, 1, 5)) => [0, 1, 2, 3, 4, 5]
    * sortArray(Arrays.asList(2, 4, 3, 0, 1, 5, 6)) => [6, 5, 4, 3, 2, 1, 0]
     */
    public List<Integer> sortArray(List<Integer> array) {
        if (array == null || array.size() <= 1) return array;

        return new ArrayList<>(new TreeSet<>(new Comparator<>(new IntegerSumComparator()))){{
            @Override
            public boolean equals(Object o) {
                return super.equals(o);
            }
            @Override
            public int hashCode() {
                return super.hashCode();
            }
        }

    }
}