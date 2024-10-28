        int sum = 0;

        for (Double num : lst) {
            sum += Math.pow(Math.ceil(num), 2);
        }

        return sum;
    }
}

Explanation:
In the given problem, we have to take the ceiling of each number in the list, square it, and add it to a running total. We can accomplish this using a for-each loop to iterate through each number in the list and the Math.ceil method to round each number to the upper integer. The Math.pow method is used to square each number. The total sum is returned at the end.

This solution has a time complexity of O(n), where n is the number of elements in the list. This is because we are iterating through each element of the list once.

In terms of space complexity, the solution is O(1), as we are only creating a single variable to store the sum. The space used does not increase with the size of the input list.
*/

// Test Cases
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        List<Double> lst1 = Arrays.asList(1.0, 2.0, 3.0);
        System.out.println(sol.sumSquares(lst1));  // Output: 14

        List<Double> lst2 = Arrays.asList(1.0, 4.0, 9.0);
        System.out.println(sol.sumSquares(lst2));  // Output: 98

        List<Double> lst3 = Arrays.asList(1.0, 3.0, 5.0, 7.0);
        System.out.println(sol.sumSquares(lst3));  // Output: 84

        List<Double> lst4 = Arrays.asList(1.4, 4.2, 0.0);
        System.out.println(sol.sumSquares(lst4));  // Output: 29

        List<