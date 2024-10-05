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
        List<Integer> sortedArray = new ArrayList<Integer>();
        int sum = 0;

        for (int i = 0; i < array.size(); i++) {
            sum += array.get(i);
        }

        if (sum % 2 == 0) {
            sortedArray = sortArray(array, true);
        } else {
            sortedArray = sortArray(array, false);
        }

        return sortedArray;
    }

    public List<Integer> sortArray(List<Integer> array, boolean ascending) {
        List<Integer> sortedArray = new ArrayList<Integer>();

        if (ascending) {
            Collections.sort(array, new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    return o1.compareTo(o2);
                }
            });
        } else {
            Collections.sort(array, new Comparator<Integer>() {
                @Override
                public int compare(Integer o1,