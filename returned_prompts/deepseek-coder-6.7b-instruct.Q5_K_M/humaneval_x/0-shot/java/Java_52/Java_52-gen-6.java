    for(int num: l){
        if(num >= t){
            return false;
        }
    }
    return true;
    }
}

The above code will iterate through the list and if any number in the list is greater or equal to the threshold, it will return false. If none of the numbers in the list are greater than or equal to the threshold, it will return true.

*/


```java

import java.util.*;

class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.belowThreshold(Arrays.asList(1, 2, 4, 10), 100)); // true
        System.out.println(sol.belowThreshold(Arrays.asList(1, 20, 4, 10), 5)); // false
    }

    public boolean belowThreshold(List<Integer> l, int t) {
        for (int num : l) {
            if (num >= t) {
                return false;
            }
        }
        return true;
    }
}
```

## Solution

The given code checks if all numbers in the list `l` are below the threshold `t`. If any number in `l` is equal to or greater than `t`, it returns `false`. Otherwise, it returns `true`.

```java
import java.util.*;

class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.belowThreshold(Arrays.asList(1, 2, 4, 10), 100)); // true
        System.out.println(sol.belowThreshold(Arrays.asList(1, 20, 4, 10), 5)); // false
    }

    public boolean belowThreshold(List<Integer> l, int t) {
        for (int num : l) {
            if (num >= t) {
                return false;
            }
        }
        return true;
    }
}
```