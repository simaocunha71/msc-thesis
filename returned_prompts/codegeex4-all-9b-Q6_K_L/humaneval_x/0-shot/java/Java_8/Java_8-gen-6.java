import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        if(numbers.isEmpty()) {
            return Arrays.asList(0, 1);
        }
        int sum = 0;
        int product = 1;
        for(int i : numbers) {
            sum += i;
            product *= i;
        }
        return Arrays.asList(sum, product);
    }
}