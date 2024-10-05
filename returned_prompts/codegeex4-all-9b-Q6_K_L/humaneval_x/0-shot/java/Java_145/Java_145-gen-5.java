import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        if (nums == null || nums.isEmpty()) {
            return Collections.emptyList();
        }

        return nums.stream()
                .sorted(Comparator.comparingInt(this::sumDigits))
                .collect(Collectors.toList());
    }

    private int sumDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

The above code defines a class `Solution` with a method `orderByPoints` that takes a list of integers as input and returns a new list sorted in ascending order based on the sum of their digits. The method `sumDigits` is used to calculate the sum of digits of a given number. The `orderByPoints` method uses Java 8 Stream API to sort the numbers based on the sum of their digits and collect them into a new list. If the input list is null or empty, the method returns an empty list.