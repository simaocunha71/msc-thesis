import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> generateIntegers(int a, int b) {
        List<Integer> evenDigits = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            if (isEvenDigit(i)) {
                evenDigits.add(i);
            }
        }
        return evenDigits;
    }

    private boolean isEvenDigit(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 != 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}