        List<Integer> rollingMax = new ArrayList<Integer>();
        int max = Integer.MIN_VALUE;
        for (int num : numbers) {
            max = Math.max(max, num);
            rollingMax.add(max);
        }
        return rollingMax;
    }
}

This solution works by iterating over the input list and maintaining the maximum number found so far. At each step, it adds the current maximum to the resulting list.

Time complexity: O(n) as it makes one pass over the input list.
Space complexity: O(n) as it needs to store the result list.

The test cases for this solution are:

assertEquals(Arrays.asList(1, 2, 3, 3, 3, 4, 4), new Solution().rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2)));
assertEquals(Arrays.asList(-1, -1, -1, 0, 0, 0, 2), new Solution().rollingMax(Arrays.asList(-1, -1, -1, 0, 0, 0, 2)));
assertEquals(Arrays.asList(2, 2, 2, 2, 2, 2, 2), new Solution().rollingMax(Arrays.asList(2, 1, 2, 1, 2, 1, 2)));
assertEquals(Arrays.asList(1), new Solution().rollingMax(Arrays.asList(1)));
assertEquals(Arrays.asList(), new Solution().rollingMax(Arrays.asList()));

This solution passes all test cases.

*/
public class Main {
    public static void main(String[] args) {
        System.out.println(new Solution().rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2)));
    }
}


A: Here's a solution using Java 8's Stream API.

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
