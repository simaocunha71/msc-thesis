import java.util.*;

class Solution {
    public List<Double> findClosestElements(List<Double> numbers) {
        // sort the list in ascending order
        Collections.sort(numbers);
        // get the length of the list
        int n = numbers.size();
        // initialize the result list
        List<Double> result = new ArrayList<>();
        // check if the list has only one element
        if (n == 1) {
            result.add(numbers.get(0));
        } else {
            // add the first and last elements of the list to the result
            result.add(numbers.get(0));
            result.add(numbers.get(n - 1));
        }
        return result;
    }
}
