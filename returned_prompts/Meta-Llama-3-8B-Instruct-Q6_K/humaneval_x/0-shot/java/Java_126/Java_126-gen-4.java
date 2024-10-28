Here is the Java code that implements the function `isSorted` as per the given requirements:

```java
import java.util.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        if (lst.size() < 2) {
            return true;
        }
        for (int i = 0; i < lst.size() - 1; i++) {
            if (lst.get(i) >= lst.get(i + 1)) {
                return false;
            }
        }
        return true;
    }
}
```

This code checks if a list of integers is sorted in ascending order. If the list has less than 2 elements, it returns `true` because a list with less than 2 elements is considered sorted. It then iterates over the list, checking if each element is less than the next one. If it finds a pair of elements where the first is not less than the second, it returns `false`, indicating that the list is not sorted. If it checks all elements without finding such a pair, it returns `true`, indicating that the list is sorted. 

Note that this code does not check for duplicate elements. If the requirement is to return `false` if there are more than one duplicate of the same number, the code needs to be modified accordingly. For example, you can add a counter to count the occurrences of each number and return `false` if any number occurs more than once. 

Here's an updated version of the code that also checks for duplicates:

```java
import java.util.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        if (lst.size() < 2) {
            return true;
        }
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : lst) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        for (int i = 0; i < lst.size() - 1; i++) {
            if (lst.get(i) >= lst.get(i + 1)) {
                return false;
            }
        }
        for (int count : countMap.values()) {
            if (count > 1) {
                return false;
            }
        }
        return true;
    }
}
```

This code first counts the occurrences of each number in the list using a `HashMap`. It then checks if the list is sorted as before. Finally, it checks if any number occurs more than once and returns