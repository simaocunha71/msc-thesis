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
        // Create a map to count the occurrences of each number
        Map<Integer, Long> countMap = numbers.stream()
                .collect(Collectors.groupingBy(n -> n, Collectors.counting()));
        
        // Filter the list to keep only numbers that occur once
        List<Integer> result = numbers.stream()
                .filter(n -> countMap.get(n) == 1)
                .collect(Collectors.toList());
        
        return result;
    }
}