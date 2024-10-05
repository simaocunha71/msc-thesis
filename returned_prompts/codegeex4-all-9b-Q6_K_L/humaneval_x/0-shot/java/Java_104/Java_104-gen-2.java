import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean hasEvenDigit = false;
            while (num > 0) {
                int digit = num % 10;
                if (digit % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
                num /= 10;
            }
            if (!hasEvenDigit) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}