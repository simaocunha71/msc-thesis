import java.util.*;
import java.lang.*;

class Solution  {

    /**
    Given a list of integers, return the sum of the two smallest integers in the list.
    If the list has less than two elements, return 0.
    >>> sumTwoSmallest([3, 5, 2, 1, 9])
    3
      */
    public int sumTwoSmallest(List<Integer> numbers) {
        if (numbers.size() < 2) {
            return 0;
        }
        Collections.sort(numbers);
        return numbers.get(0) + numbers.get(1);
    }
}

