        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if (i < numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }

}

The function intersperse takes a list of integers and an integer delimiter as input and returns a new list where the delimiter is inserted between every two consecutive numbers from the input list. 

If the input list is empty, the function simply returns an empty list.

In the function, we iterate over the input list. For each number in the list, we add it to the result list. Then, if we are not at the last number in the list, we also add the delimiter to the result list. 

The final result list is then returned as the output of the function.

The time complexity of the function is O(n) where n is the length of the input list. The space complexity is also O(n) because we are storing the result in a new list.

This function can be used in a variety of scenarios where you want to insert a delimiter between every two consecutive elements of a list. For example, it can be used to format a list of numbers for display, or to insert a delimiter between words in a sentence.
    */

// Test cases

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1: empty list
        List<Integer> numbers1 = new ArrayList<>();
        int delimiter1 = 4;
        System.out.println(solution.intersperse(numbers1, delimiter1));  // []

        // Test case 2: list with multiple elements
        List<Integer> numbers2 = Arrays.asList(1, 2, 3);
        int delimiter2 = 4;
        System.out.println(solution.intersperse(numbers2, delimiter2));  // [1, 4, 2, 4, 3