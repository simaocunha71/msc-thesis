First, we create an array a of length n. For each i  (1 <= i <= n), we calculate the value of a[i] = i * i - i + 1.

B:
Then, we go through each pair of i, j, k such that i < j < k. If the sum of a[i], a[j], and a[k] is a multiple of 3, we increment our count.

Finally, we return the count.

This solution has a time complexity of O(n^3) due to the 3 nested loops, making it inefficient for large inputs.

Is there a way to optimize this solution?

*/

// C:
import java.util.*;

class Solution {
    public int getMaxTriples(int n) {
        int[] a = new int[n];
        for (int i = 1; i <= n; i++) {
            a[i - 1] = i * i - i + 1;
        }

        int[] remainderCounts = new int[3];
        for (int i = 0; i < n; i++) {
            remainderCounts[a[i] % 3]++;
        }

        int count = remainderCounts[0] * (remainderCounts[0] - 1) * (remainderCounts[0] - 2) / 6;
        count += remainderCounts[1] * (remainderCounts[