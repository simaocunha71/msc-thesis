```java
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
        // Convert the input list to an array for easy manipulation
        Integer[] arr = nums.toArray(new Integer[0]);

        // Sort the array using a custom comparator
        Arrays.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                // Calculate the sum of digits for both integers
                int sumA = sumOfDigits(a);
                int sumB = sumOfDigits(b);

                // Compare the sums of digits
                if (sumA != sumB) {
                    return sumA - sumB;
                } else {
                    // If the sums are equal, compare the original indices
                    return nums.indexOf(a) - nums.indexOf(b);
                }
            }
        });

        // Convert the sorted array back to a list and return it
        return Arrays.asList(arr);
    }

    // Helper method to calculate the sum of digits of an integer
    private int sumOfDigits(int num) {
        int sum = 0;
        String str = Integer.toString(Math.abs(num));
        for (int i = 0; i < str.length(); i++) {
            sum += Character.getNumericValue(str.charAt(i));
        }
        return sum;
    }
}
```