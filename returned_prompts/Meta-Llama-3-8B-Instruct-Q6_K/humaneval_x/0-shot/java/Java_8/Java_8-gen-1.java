import java.util.*;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for (int num : numbers) {
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }
}
Explanation:
We iterate through the list of numbers and calculate the sum and product of the numbers. We initialize sum to 0 and product to 1. For each number in the list, we add the number to sum and multiply the number with product. Finally, we return a list containing the sum and product. If the list is empty, sum will be 0 and product will be 1, as per the problem statement. 