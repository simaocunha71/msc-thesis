import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    /**
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> removeDuplicates(Array.asList(1, 2, 3, 2, 4))
    [1, 3, 4]
     */
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        List<Integer> res = new ArrayList<>();
        for (int i : numbers) {
            if (!res.contains(i)) {
                res.add(i);
            }
        }
        return res;
    }
}