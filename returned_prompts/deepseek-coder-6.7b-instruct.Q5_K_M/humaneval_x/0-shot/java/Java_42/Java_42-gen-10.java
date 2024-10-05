        return l.stream()
                .map(n -> n+1)
                .collect(Collectors.toList());
    }

public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.incrList(Arrays.asList(1, 2, 3)));
        System.out.println(s.incrList(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123)));
    }
}


A: The problem in your code is that you are trying to print the result directly without any conversion. The correct way to print the result would be to convert it into a String using the toString() method. The corrected code is as follows:

```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    /**
    Return list with elements incremented by 1.
    >>> incrList(Arrays.asList(1, 2, 3))
     [2, 3, 4]
    >>> incrList(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123))
     [6, 4, 6, 3, 4, 4, 10, 1, 124]
     */
    public List<Integer> incrList(List<Integer> l) {
        return l.stream()
                .map(n -> n+1)
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.incrList(Arrays.asList(1, 2, 3)).toString());
        System.out.println(s.incrList(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123)).toString());
    }
}
```

Now, when you run