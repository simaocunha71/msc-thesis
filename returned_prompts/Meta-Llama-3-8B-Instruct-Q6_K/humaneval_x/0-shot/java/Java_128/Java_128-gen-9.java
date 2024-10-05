    import java.util.*;
import java.lang.*;

public class Solution {
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
            int sign = num / Math.abs(num);
            signProduct *= sign;
            sumOfMagnitudes += Math.abs(num);
        }
        return Optional.of(signProduct * sumOfMagnitudes);
    }
}