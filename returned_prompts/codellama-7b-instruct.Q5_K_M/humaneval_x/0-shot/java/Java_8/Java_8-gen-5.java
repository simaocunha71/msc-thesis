import java.util.*;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for (Integer i : numbers) {
            sum += i;
            product *= i;
        }
        return Arrays.asList(sum, product);
    }
}
