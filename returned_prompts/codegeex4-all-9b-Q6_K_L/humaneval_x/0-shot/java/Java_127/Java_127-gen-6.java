To determine if the length of intersection between two intervals is a prime number, we need to follow these steps:

1. Find the start and end of the intersection.
2. Calculate the length of the intersection.
3. Check if the length is a prime number.

Here is the complete code:

```java
import java.util.*;

class Solution {
    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        // Step 1: Find the start and end of the intersection
        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        
        // Step 2: Calculate the length of the intersection
        int length = end - start + 1;
        
        // Step 3: Check if the length is a prime number
        if (length < 2) {
            return "NO";
        }
        for (int i = 2; i < Math.sqrt(length); i++) {
            if (length % i == 0) {
                return "NO";
            }
        }
        return "YES";
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.intersection(Arrays.asList(1, 2), Arrays.asList(2, 3))); // NO
        System.out.println(solution.intersection(Arrays.asList(-1, 1), Arrays.asList(0, 4))); // NO
        System.out.println(solution.intersection(Arrays.asList(-3, -1), Arrays.asList(-5, 5))); // YES
    }
}
```

The `intersection` method takes two intervals as input, represented as lists of integers. It first finds the start and end of the intersection by taking the maximum of the start points and the minimum of the end points of the two intervals. Then, it calculates the length of the intersection by subtracting the start from the end and adding 1. Finally, it checks if the length is a prime number by iterating from 2 to the square root of the length and checking if it is divisible by any number. If it is divisible, it returns "NO", otherwise, it returns "YES".

The `main` method is used to test the `intersection` method with the provided examples.