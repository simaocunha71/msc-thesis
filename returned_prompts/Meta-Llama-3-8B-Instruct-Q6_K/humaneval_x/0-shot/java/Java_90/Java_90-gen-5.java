    import java.util.*;
import java.util.stream.*;

public class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) {
            return Optional.empty();
        }
        Optional<Integer> smallest = lst.stream().min(Integer::compareTo);
        if (smallest.isPresent() && smallest.get() == lst.get(0)) {
            return lst.stream().filter(i -> i != smallest.get()).min(Integer::compareTo);
        }
        return Optional.empty();
    }
}

Explanation:
The function nextSmallest() takes a list of integers as input and returns the 2nd smallest element if it exists, otherwise it returns an empty Optional.

Firstly, it checks if the list has less than 2 elements. If it does, it returns an empty Optional.

Then, it finds the smallest element in the list using the min() function and the compareTo() method. If the smallest element is the first element in the list, it means that the list has only one unique element, so it returns an empty Optional.

Finally, if the smallest element is not the first element, it finds the 2nd smallest element by filtering out the smallest element and then finding the minimum of the remaining elements.

This solution uses Java 8's Stream API to make the code more concise and efficient. The min() function and the filter() function are used to find the smallest and 2nd smallest elements respectively. The compareTo() method is used to compare the elements in the list. The Optional class is used to handle the case where there is no 2nd smallest element.