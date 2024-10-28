
Your first function is pretty good, but you can make it faster by not using a nested loop.  It's not necessary to compare each element to every other element.  You can use a TreeSet to sort the list and then just check if the next element is within the threshold.  This should be faster because the TreeSet is implemented as a binary tree, so each lookup is O(log n) rather than O(n).
import java.util.*;

class Solution {
    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
     */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        Set<Double> sortedNumbers = new TreeSet<>(numbers);
        Double last = null;
        for (Double number : sortedNumbers) {
            if (last != null && Math.abs(number - last) < threshold) {
                return true;
            }
            last = number;
        }
        return false;
    }
}

Your second function is also pretty good, but you can make it faster by using a StringBuilder to build the current string.  This is because StringBuilder is more efficient than concatenating strings using the + operator.
import java.util.*;

class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
