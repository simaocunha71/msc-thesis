import java.util.*;
import java.lang.*;

class Solution {
    /**
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse(List.of(), 4)
    []
    >>> intersperse(Arrays.asList(1, 2, 3), 4)
    [1, 4, 2, 4, 3]
     */
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        List<Integer> result = new ArrayList<>();
        if (numbers.size() == 0) {
            return result;
        }
        for (int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if (i != numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }

    /**
    Return a new list with the elements of `numbers' in reverse order
    >>> reverse(List.of())
    []
    >>> reverse(Arrays.asList(1, 2, 3))
    [3, 2, 1]
     */
    public List<Integer> reverse(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        for (int i = numbers.size() - 1; i >= 0; i--) {
            result.add(numbers.get(i));
        }
        return result;
    }

    /**
    Return a new list with the elements of `numbers' in sorted order
    >>> sorted(List.of())
    []
    >>> sorted(Arrays.asList(3, 2, 1))
    [1, 2, 3]
     */
    public List<Integer> sorted(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
        }
        return result;
    }
}
