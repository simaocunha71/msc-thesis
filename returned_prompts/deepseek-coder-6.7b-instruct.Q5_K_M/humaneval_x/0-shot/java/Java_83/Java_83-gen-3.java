        int count = 0;
        if (n == 1) {
            return 2;
        } else {
            for (int i = 1; i <= n; i++) {
                if (i == 1 || i == n) {
                    count += Math.pow(10, i - 1) * 2;
                } else {
                    count += Math.pow(10, i - 1) * 4;
                }
            }
        }
        return count;
    }
}

The solution works for n > 1, but it doesn't account for numbers with leading zeros. 
So, if n = 2, it will return 30 (20 numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200)
which is incorrect. 

The correct solution should look like this:

import java.util.*;
import java.lang.*;

class Solution  {
    public int startsOneEnds(int n) {
        if (n == 1) {
            return 2;
        } else {
            int count = 0;
            for (int i = 1; i <= n; i++) {
                if (i == 1 || i == n) {
                    count += (int)Math.pow(9, n - 1);
                } else {
                    count += (int)Math.pow(9, n - i) * 2;
                }
            }
            return count;
        }
    }
}

This solution correctly accounts for numbers with leading zeros.

The number of n-digit numbers that start with 1 is 9 * 10^(n-2) if n > 1, and 1 if n = 1.
The number of n-digit numbers that end with 1 is 9 * 10^(n-2) if n > 1, and 1