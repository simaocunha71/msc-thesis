    import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int signProduct = 1;
        int sumOfMagnitudes = 0;

        for (int num : arr) {
            if (num == 0) {
                return Optional.empty();
            }
            signProduct *= Math.signum(num);
            sumOfMagnitudes += Math.abs(num);
        }

        return Optional.of(signProduct * sumOfMagnitudes);
    }
}
The code defines a class called `Solution` with a method `prodSigns` that takes a list of integers as input and returns an `Optional<Integer>` representing the sum of magnitudes of integers multiplied by the product of all signs of each number in the array.

The method first checks if the input array is empty. If it is, it returns an empty `Optional`.

Then, it initializes two variables: `signProduct` to keep track of the product of all signs, and `sumOfMagnitudes` to keep track of the sum of magnitudes of integers.

It then iterates over the input array. For each number, it checks if the number is zero. If it is, it returns an empty `Optional` because the product of signs is undefined for an array containing zero.

If the number is not zero, it updates the `signProduct` by multiplying it with the sign of the number (using the `Math.signum` method, which returns 1 for positive numbers, -1 for negative numbers, and 0 for zero), and updates the `sumOfMagnitudes` by adding the absolute value of the number (using the `Math.abs` method).

Finally, it returns an `Optional<Integer>` containing the product of `signProduct` and `sumOfMagnitudes`. If the input array is not empty and contains no zeros, this will be the desired result. If the input array is empty or contains a zero, this will be an empty `Optional`.