        Collections.sort(l);
        int len = l.size();
        if (len % 2 == 0)
            return ((double)l.get(len/2) + l.get(len/2 - 1))/2;
        else
            return (double) l.get(len/2);
    }
}

The solution sorts the list and then checks if the length of the list is even or odd. If it's even, the median is the average of the two middle numbers, if it's odd, the median is the middle number.

The time complexity is O(n log n) due to the sorting and the space complexity is O(1) as no extra space is required.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int len = l.size();
        if (len % 2 == 0)
            return ((double)l.get(len/2) + l.get(len/2 - 1))/2;
        else
            return (double) l.get(len/2);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.median(Arrays.asList(3, 1, 2, 4, 5))); // 3.0
        System.out.println(sol.median(Arrays.asList(-10, 4, 6, 1000, 10, 20))); // 15.0
    }
}



















































































































