        if(n == 0) return 0;
        if(n == 1) return 0;
        if(n == 2) return 1;

        int[] fibfibArray = new int[n+1];
        fibfibArray[0] = 0;
        fibfibArray[1] = 0;
        fibfibArray[2] = 1;

        for(int i = 3; i <= n; i++){
            fibfibArray[i] = fibfibArray[i-1] + fibfibArray[i-2] + fibfibArray[i-3];
        }

        return fibfibArray[n];
    }
}

Here, we are storing the fibfib numbers in an array and for each number greater than 2, we are adding the previous, second previous and third previous fibfib numbers to compute the current fibfib number. The time complexity is O(n) and the space complexity is O(n).

*/


import java.util.*;
import java.lang.*;

class Solution  {
    public int fibfib(int n)  {
        if(n == 0) return 0;
        if(n == 1) return 0;
        if(n == 2) return 1;

        int[] fibfibArray = new int[n+1];
        fibfibArray[0] = 0;
        fibfibArray[1] = 0;
        fibfibArray[2] = 1;

        for(int i = 3; i <= n; i++){
            fibfibArray[i] = fibfibArray[i-1] + fibfibArray[i-2] + fibfibArray[i-3];
        }

        return fibfibArray[n];
    }
}


















































































