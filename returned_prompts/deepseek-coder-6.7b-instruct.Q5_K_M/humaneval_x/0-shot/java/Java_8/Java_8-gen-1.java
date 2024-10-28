        int sum = 0;
        int product = 1;
        for(int num : numbers){
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }

}

This solution works by iterating over the provided list of integers and updating a running sum and product. The running sum and product are then returned as a list.
*/

import java.util.*;

class Solution {
    public static List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for(int num : numbers){
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }

    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
        List<Integer> result = sumProduct(numbers);
        System.out.println(result);  // Output: [10, 24]
    }
}

/*
Output:
[10, 24]
*/

/*
