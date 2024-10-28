        List<Integer> intList = new ArrayList<Integer>();
        for (Object obj : values) {
            if (obj instanceof Integer) {
                intList.add((Integer) obj);
            }
        }
        return intList;
    }
}


A: import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> filterIntergers(List<Object> values) {
        List<Integer> intList = new ArrayList<Integer>();
        for (Object obj : values) {
            if (obj instanceof Integer) {
                intList.add((Integer) obj);
            }
        }
        return intList;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Object> list = Arrays.asList('a', 3.14, 5, 1, 2, 3, "abc", new HashMap<>(), new ArrayList<>());
        List<Integer> result = solution.filterIntergers(list);
        System.out.println(result); // [5, 1, 2, 3]
    }
}


A: Here is the correct way to solve the problem:

```java

import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> filterIntegers(List<Object> values) {
        List<Integer> intList = new ArrayList<Integer>();
        for (Object obj : values) {
            if (obj instanceof Integer) {
                intList.add((Integer) obj);
            }
        }
        return intList;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Object> list = Arrays.asList('a', 3.14, 5, 1, 2, 3, "abc", new HashMap<>(), new ArrayList<>());
        List<Integer> result = solution.filterIntegers(list);
        System.out.println(result); // [5, 1, 2, 3]
    }
}
```

The main method in the