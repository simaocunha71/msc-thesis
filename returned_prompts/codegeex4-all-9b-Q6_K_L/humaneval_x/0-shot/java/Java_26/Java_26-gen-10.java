import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        // Use a set to keep track of unique elements
        Set<Integer> uniqueNumbers = new HashSet<>();

        // Use a list to keep track of the order of elements
        List<Integer> result = new ArrayList<>();

        // Iterate over the input list
        for (Integer number : numbers) {
            // If the number is not in the set, add it to the result list and the set
            if (!uniqueNumbers.contains(number)) {
                result.add(number);
                uniqueNumbers.add(number);
            }
        }

        return result;
    }
}