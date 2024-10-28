import java.util.*;
import java.lang.*;

class Solution {
    /**
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> removeDuplicates(Array.asList(1, 2, 3, 2, 4))
    [1, 3, 4]
     */
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        List<Integer> uniqueNumbers = new ArrayList<>();
        numbers.forEach(number -> {
            if (!uniqueNumbers.contains(number)) {
                uniqueNumbers.add(number);
            }
        });
        return uniqueNumbers;
    }
}

