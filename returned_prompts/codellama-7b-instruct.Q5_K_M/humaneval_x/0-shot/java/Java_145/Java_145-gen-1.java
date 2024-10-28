import java.util.*;

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
        // write your code here
        Comparator<Integer> comparator =
                Comparator.comparingInt(num -> {
                    String str = String.valueOf(num);
                    int sum = 0;
                    for (int i = 0; i < str.length(); i++) {
                        sum += str.charAt(i) - '0';
                    }
                    return sum;
                }).thenComparingInt(nums::indexOf);
        nums.sort(comparator);
        return nums;
    }
}

B:
import java.util.*;

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
        // write your code here
        Comparator<Integer> comparator =
                Comparator.comparingInt(num -> {
                    String str = String.valueOf(num);
                    int sum = 0;
                    for (int