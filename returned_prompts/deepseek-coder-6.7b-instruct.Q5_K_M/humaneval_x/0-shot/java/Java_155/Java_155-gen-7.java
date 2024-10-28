        List<Integer> result = new ArrayList<>(Arrays.asList(0, 0));
        num = Math.abs(num);

        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                result.set(0, result.get(0) + 1);
            } else {
                result.set(1, result.get(1) + 1);
            }
            num /= 10;
        }
        return result;
    }
}

You can also consider using a string to convert the number to a sequence of characters, then loop through each character to determine if it is odd or even.

A: import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        evenOddCount(-12) ==> (-1, 2)
        evenOddCount(123) ==> (1, 2)
      */
    public List<Integer> evenOddCount(int num) {
        List<Integer> result = new ArrayList<>(Arrays.asList(0, 0));
        num = Math.abs(num);

        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                result.set(0, result.get(0) + 1);
            } else {
                result.set(1, result.get(1) + 1);