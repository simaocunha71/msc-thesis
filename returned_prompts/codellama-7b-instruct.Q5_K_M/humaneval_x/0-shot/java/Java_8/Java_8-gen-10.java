import java.util.*;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for (int i = 0; i < numbers.size(); i++) {
            sum += numbers.get(i);
            product *= numbers.get(i);
        }
        return Arrays.asList(sum, product);
    }
}
