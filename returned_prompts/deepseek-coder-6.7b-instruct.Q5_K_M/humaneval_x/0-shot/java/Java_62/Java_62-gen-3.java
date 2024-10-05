        List<Integer> result = new ArrayList<>();
        for(int i = 1; i < xs.size(); i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}

The solution is simple, we just need to iterate through the list from the second element (since the first one is a constant and the derivative of a constant is 0) to the end, multiply the current coefficient by its degree, and add it to the result list.
The result list is returned at the end.
*/

// Another solution by using Java 8 Stream API

import java.util.*;
import java.util.stream.*;

class Solution {
    public List<Integer> derivative(List<Integer> xs) {
        return IntStream.range(1, xs.size())
                        .map(i -> i * xs.get(i))
                        .boxed()
                        .collect(Collectors.toList());
    }
}

// This solution is more concise and readable than the previous one. It uses the Java 8 Stream API to perform the same operations in a more functional style. The range method generates a stream of integers from 1 to the size of the input list, the map method multiplies each integer by its corresponding coefficient in the input list, the boxed method converts the stream of ints to a stream of Integer, and the collect method converts the stream back to a list.

// Test Cases

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.derivative(Arrays.asList(3, 1, 2, 4, 5))); // [1, 4, 12, 20]
        System.out.println(sol.derivative(Arrays.asList(1, 2, 3))); // [2, 6]
    }
}

// This will print the derivatives of the two given polynomials.

*/

//src/main/java/com/example/java/questions/polymorphism/Dog.java
package com