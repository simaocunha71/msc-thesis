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
        List<Integer> sorted = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (countOnes(arr.get(i)) == countOnes(arr.get(j)) && arr.get(i) > arr.get(j)) {
                    int temp = arr.get(i);
                    arr.set(i, arr.get(j));
                    arr.set(j, temp);
                }
            }
        }
        for (int i = 0; i < arr.size(); i++) {
            if (countOnes(arr.get(i)) == 0 && sorted.size() == 0) {
                sorted.add(arr.get(i));
            } else if (countOnes(arr.get(i)) == 0 && sorted.size() != 0 && sorted.get(sorted.size() - 1) > arr.get(i)) {
                sorted.add(arr.get(i));
            } else if (countOnes(arr