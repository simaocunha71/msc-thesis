    import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for (int num : numbers) {
            sum += num;
            product *= num;
        }
        List<Integer> result = new ArrayList<>();
        result.add(sum);
        result.add(product);
        return result;
    }
}

Explanation:
The problem is asking to create a method that takes a list of integers as input and returns a list containing the sum and product of all the integers in the list.

The method iterates over the input list, adding each number to the sum and multiplying each number to the product. If the input list is empty, the sum is 0 and the product is 1, as specified.

Finally, the method returns a list containing the sum and product. The sumProduct method is implemented in the Solution class.

This solution has a time complexity of O(n), where n is the size of the input list, since it iterates over the list once. The space complexity is O(1), since it only uses a constant amount of space to store the sum and product.