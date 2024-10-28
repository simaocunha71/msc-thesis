        int count = 0;
        int[] arr = new int[n];

        for (int i = 1; i <= n; i++) {
            arr[i-1] = i * i - i + 1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k < n; k++) {
                    if ((arr[i] + arr[j] + arr[k]) % 3 == 0) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
}

Here, I have used a triple loop to check every possible triple of indices in the array. If the sum of the values at those indices is divisible by 3, I increment the count. Finally, I return the count. The time complexity of this solution is O(n^3), which is acceptable for small n.

This solution works by first generating the array as per the given condition. Then, it iterates over all possible triples of indices in the array. For each triple, it checks if the sum of the values at those indices is divisible by 3. If so, it increments the count. Finally, it returns the count.
    */
}

//src/main/java/com/example/demo/service/impl/SolutionImpl.java
package com.example.demo.service.impl;

import com.example.demo.service.Solution;
import org.springframework.stereotype.Service;

@Service
public class SolutionImpl implements Solution {

    @Override
    public int getMaxTriples(int n) {
        int count = 0;
        int[] arr = new int[n];

        for (int i = 1; i <= n; i++) {
            arr[i-1] = i * i - i + 1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k <