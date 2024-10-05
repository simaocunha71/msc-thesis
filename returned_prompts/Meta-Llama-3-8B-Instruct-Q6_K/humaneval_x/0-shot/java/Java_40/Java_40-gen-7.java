Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<>();
        for (int num : l) {
            set.add(num);
        }

        for (int num1 : set) {
            for (int num2 : set) {
                int complement = -num1 - num2;
                if (set.contains(complement)) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

The solution works by first converting the list to a set to remove duplicates. Then, it iterates over the set to find three numbers that sum to zero. It does this by iterating over each number in the set, and for each number, it calculates the complement (the number that would be needed to sum to zero). It then checks if the complement is in the set. If it is, it returns true, indicating that there are three numbers in the list that sum to zero. If it doesn't find any such numbers, it returns false. This solution has a time complexity of O(n^2), where n is the number of elements in the list. This is because it has to iterate over the list twice, once to convert it to a set and once to find the triplets. The space complexity is O(n), because it has to store the set. This solution is efficient for small to medium-sized lists, but for large lists, it may be slow. In that case, a more efficient solution would be needed.