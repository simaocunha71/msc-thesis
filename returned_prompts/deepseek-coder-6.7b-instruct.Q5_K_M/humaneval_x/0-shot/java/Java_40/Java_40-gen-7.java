        int n = l.size();
        HashSet<Integer> hs = new HashSet<Integer>();
        for (int i = 0; i < n; i++)
            hs.add(l.get(i));
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int sum = l.get(i) + l.get(j);
                if (hs.contains(-sum))
                    return true;
            }
        }
        return false;
    }
}


A: In your solution, you are iterating over the list twice, which makes the time complexity of your solution O(n^2). You can improve it by using a single pass through the list, while also using a HashMap to store the sum of pairs of elements. Here is a more efficient solution:

```java
import java.util.*;

class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        int n = l.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int sum = l.get(i) + l.get(j);
                if (!map.containsKey(sum)) {
                    map.put(sum, new ArrayList<>());
                }
                map.get(sum).add(new int[] {i, j});
            }
        }
        for (int i = 0; i < n; i++) {
            if (map.containsKey(-l.get(i))) {
                for (int[] pair : map.get(-l.get(i))) {
                    if (pair[0] != i && pair[1] != i) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
```

In this solution, we use a HashMap to store the sum of pairs of elements from the list. For each pair of elements, we add their indices to the corresponding