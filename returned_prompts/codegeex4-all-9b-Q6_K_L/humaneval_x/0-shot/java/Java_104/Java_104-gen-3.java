import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            if (hasEvenDigit(i)) {
                continue;
            }
            result.add(i);
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasEvenDigit(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
}