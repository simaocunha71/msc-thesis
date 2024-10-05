        int count = 0;

        for (int i = 0; i < arr.size(); i++) {
            int sum = 0;
            String number = Integer.toString(arr.get(i));

            for (int j = 0; j < number.length(); j++) {
                char c = number.charAt(j);
                int digit = Character.getNumericValue(c);

                if (c == '-') {
                    j++;
                }

                sum += digit;
            }

            if (sum > 0) {
                count++;
            }
        }

        return count;
    }
}


A: import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Write a function countNums which takes an array of integers and returns
    the number of elements which has a sum of digits 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> countNums(Arrays.asList()) 
    0
    >>> countNums(Arrays.asList(-1, 11, -11)) 
    1
    >>> countNums(Arrays.asList(1, 1, 2)) 
    2
     */
    public int countNums(List<Integer> arr)  {
        int count = 0;

        for (int i = 0; i < arr.size(); i++) {
            int sum = 0;
            String number = Integer.toString(arr.get(i));

            for (int j = 0; j < number.length(); j++) {
                char c = number.charAt(j);
                int digit = Character.getNumericValue(c);

                if (c == '-') {
                    j++;
                }

                sum += digit;
            }

            if (sum == 0) {
                count++;
            }
        }

        return count;
    }
}


A: import java.util.*;
import java.lang.*;