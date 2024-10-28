        List<Integer> result = new ArrayList<>();
        if (lst.isEmpty()) {
            return result;
        }
        Collections.sort(lst);
        while (!lst.isEmpty()) {
            result.add(lst.remove(0));
            if (!lst.isEmpty()) {
                result.add(lst.remove(lst.size() - 1));
            }
        }
        return result;
    }
}

The code above works by sorting the input list and then repeatedly removing the smallest and largest elements from the list, adding them to a new list, until the input list is empty. The resulting new list is then returned as the result.

It's important to note that this code assumes that the input list contains at least one integer. If the input list can be empty, the code should be modified to handle this case by returning an empty list at the beginning of the function.
    */


A: Here's how you could do it:

```java
import java.util.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        List<Integer> result = new ArrayList<>();
        if (lst.isEmpty()) {
            return result;
        }
        Collections.sort(lst);
        while (!lst.isEmpty()) {
            result.add(lst.remove(0)); // add smallest
            if (!lst.isEmpty()) {
                result.add(lst.remove(lst.size() - 1)); // add largest
            }
        }
        return result;
    }
}
```

This code sorts the input list and then repeatedly removes the smallest and largest elements from the list, adding them to the result list until the input list is empty. The result list is then returned. If the input list is empty, an empty list is returned.

Here's how you could use it:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> input = Arrays.asList(4, 3, 2, 1);
    System.out.println(solution.strangeSortList(input)); //