import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
     */
    public int fib(int n) {
        if (n <= 0) return 0;
        // 从i=4开始，每次都要总和一个前者，如果是第5次，则需要累加到第4次的结果。所以最后应该是累乘数字n^2-1
        int[] f = new int[n]; // 因为这种写法可能会有误差，建议改成int[] f = new int [n+1]
        for(int i=4;i<=n;i++){
            if (i%2 == 0){
                f[i-3] += f[i-2];
            }else{
                f[i-4] = f[i-3]+f[i-2];
            }
        }
        return f[n-1]; // 快速计算下去，并返回结果
    }
}