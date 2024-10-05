        if(n==0 || n==1){
            return 0;
        }
        if(n==2){
            return 1;
        }
        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 1;
        for(int i=3; i<=n; i++){
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
        }
        return fib[n];
    }
}


A: Here is an alternative solution using memoization. Instead of using an array, we can use a HashMap to store the computed values. This way we avoid the overhead of array creation and access.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<Integer, Integer> memo;

    public Solution() {
        this.memo = new HashMap<>();
        this.memo.put(0, 0);
        this.memo.put(1, 0);
        this.memo.put(2, 1);
    }

    public int fibfib(int n) {
        if (this.memo.containsKey(n)) {
            return this.memo.get(n);
        } else {
            int result = fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3);
            this.memo.put(n, result);
            return result;
        }
    }
}
```

This solution has a time complexity of O(n) and a space complexity of O(n), which is better than the previous solution. The HashMap stores the computed values, so we don't have to recompute them when we need them later.

It's important to note that this solution assumes that the input n is non-negative. If n can be negative, we would need to handle that case separately.

Also, this solution assumes that n is not too large, as the HashMap could become very large if n is very large. If n