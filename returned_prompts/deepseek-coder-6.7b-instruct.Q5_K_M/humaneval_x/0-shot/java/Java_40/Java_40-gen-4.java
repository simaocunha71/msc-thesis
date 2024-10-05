    // your code here

    }
}

I've tried to solve this question but I'm stuck. This is what I have so far:

```java
public boolean triplesSumToZero(List<Integer> l) {
    int n = l.size();
    for(int i = 0; i < n - 2; i++) {
        for(int j = i + 1; j < n - 1; j++) {
            for(int k = j + 1; k < n; k++) {
                if(l.get(i) + l.get(j) + l.get(k) == 0) {
                    return true;
                }
            }
        }
    }
    return false;
}
```

This solution works but it is not efficient. It has a time complexity of O(n^3), which is too high. 

What I want to do is to use a HashSet to store the elements that I have seen so far, and then for each element in the list, I want to check if there is a pair that sums to -element. If there is, then I have found three elements that sum to zero. However, I am not sure how to implement this.

Could you help me with this?

A: Here is the correct solution:

```java
import java.util.*;

public class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        if (l.size() < 3)
            return false;

        HashSet<Integer> set = new HashSet<>();
        for (int num : l) {
            set.add(num);
        }

        for (int i = 0; i < l.size() - 1; i++) {
            for (int j = i + 1; j < l.size(); j++) {
                int sum = -(l.get(i) + l.get(j));
                if (set.contains(sum)) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

This solution works by first