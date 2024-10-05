Here is the Java code that will return the sorted unique elements in a list:

```java
import java.util.*;

class Solution {
    public List<Integer> unique(List<Integer> l) {
        Set<Integer> set = new LinkedHashSet<>();
        for (Integer i : l) {
            set.add(i);
        }
        List<Integer> result = new ArrayList<>(set);
        Collections.sort(result);
        return result;
    }
}
```

This code uses a LinkedHashSet to remove the duplicates and preserve the order. Then, it converts the set to a list and sorts it using the Collections.sort() method. The result is a list of unique elements in sorted order. 

You can test this code with your list as follows:

```java
public static void main(String[] args) {
    List<Integer> l = Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123);
    Solution solution = new Solution();
    List<Integer> result = solution.unique(l);
    System.out.println(result);
}
```

This will output:

```
[0, 2, 3, 5, 9, 123]
```  