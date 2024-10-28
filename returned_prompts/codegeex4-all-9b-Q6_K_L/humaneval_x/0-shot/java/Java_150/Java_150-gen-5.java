```java
import java.util.*;
import java.lang.*;

class Solution {
    public int xOrY(int n, int x, int y) {
        if(isPrime(n)) {
            return x;
        } else {
            return y;
        }
    }

    private boolean isPrime(int n) {
        if(n <= 1) {
            return false;
        }
        for(int i = 2; i <= Math.sqrt(n); i++) {
            if(n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```