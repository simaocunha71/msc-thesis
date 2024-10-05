        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = (i+1)*(i+1) - (i+1) + 1;
        }

B:
        int count = 0;
        for(int i=0; i<n-2; i++){
            for(int j=i+1; j<n-1; j++){
                for(int k=j+1; k<n; k++){
                    if((arr[i] + arr[j] + arr[k]) % 3 == 0)
                        count++;
                }
            }
        }
        return count;
    }

}

Question:
Here, I have implemented a code snippet in Java that calculates a[i] for each i from 1 to n, where a[i] = i*i - i + 1. Then, I use three nested loops to iterate through all possible combinations of three numbers. If the sum of the three numbers is a multiple of 3, I increment the count. Finally, I return the count.

This code snippet seems to work correctly, but I'm not sure if it's the most efficient way to solve this problem. Could you please suggest a more efficient approach?

A: Here is a more efficient approach using a hashmap to store the frequency of each remainder when divided by 3. This way, instead of checking every possible triplet, we can just check for pairs that sum to a multiple of 3. 

This approach reduces the time complexity from O(n^3) to O(n^2), which is a significant improvement.

Here is the Java code:

```java
import java.util.*;

class Solution {
    public int getMaxTriples(int n) {
        int[] a = new int[n+1];
        for(int i = 1; i <= n; i++) {
            a[i] = i*i - i + 1;
        }

        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 1; i <= n; i++) {
            int remainder = a[i] %