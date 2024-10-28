        if (n > m) {
            return -1;
        }

        int sum = 0;
        for(int i = n; i <= m; i++) {
            sum += i;
        }

        int avg = (int)Math.round((double)sum/(m-n+1));

        return Integer.toBinaryString(avg);
    }

}

//This solution works well but it can be optimized. The sum can be calculated in one line using the formula for the sum of an arithmetic series: (m - n + 1) * (n + m) / 2. And then we can calculate the average in one line.

import java.util.*;
import java.lang.*;

class Solution  {
    public Object roundedAvg(int n, int m)  {
        if (n > m) {
            return -1;
        }

        long sum = (long)(m - n + 1) * (n + m) / 2;
        int avg = (int)Math.round(sum/(double)(m-n+1));

        return Integer.toBinaryString(avg);
    }
}

//This is a more optimized solution. It calculates the sum of the numbers in one line and then calculates the average in one line. It also casts the sum to a long to avoid overflow, and it returns "-1" if n > m.

//This solution uses the Integer.toBinaryString() method to convert the average to binary.

//This solution also uses type casting (long) to avoid overflow when calculating the sum of the numbers.

//This solution uses the Math.round() method to round the average to the nearest integer.

//This solution uses the for loop to calculate the sum of the numbers from n to m.

//This solution uses the Integer.toBinaryString() method to convert the rounded average to a binary string.

//This solution returns "-1" if n > m, otherwise it returns the binary string of the rounded average.

//This solution has a time complexity of O((m-n+1)^2) due to the for loop and a space complexity of O(1) due to the constant amount of variables used.

//