    import java.util.*;

public class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for (int number : numbers) {
            sum += number;
            product *= number;
        }
        List<Integer> result = new ArrayList<>();
        result.add(sum);
        result.add(product);
        return result;
    }
}
// Test the method
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
        List<Integer> result = solution.sumProduct(numbers);
        System.out.println(result); // prints [10, 24]
    }
}
// Output: [10, 24]
// It will calculate the sum and product of all the numbers in the list and return them in a list. If the list is empty, it will return [0, 1]. If the list contains one element, it will return [element, element]. If the list contains multiple elements, it will return a list with the sum of all elements as the first element and the product of all elements as the second element.