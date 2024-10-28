        List<Integer> sortedList = new ArrayList<Integer>(lst);
        Collections.sort(sortedList);

        if(sortedList.size() < 2){
            return Optional.empty();
        }

        return Optional.of(sortedList.get(1));
    }
}

The above code first sorts the given list of integers in ascending order. If the size of the list is less than 2, it returns an empty Optional as there is no second smallest element. If there are at least 2 elements in the list, it returns the second element, which is the second smallest in the original unsorted list.

Alternative solution:
```java
public Optional<Integer> nextSmallest(List<Integer> lst) {
    if (lst.size() < 2) {
        return Optional.empty();
    }

    int min = Integer.MAX_VALUE;
    int secondMin = Integer.MAX_VALUE;

    for (int num : lst) {
        if (num < min) {
            secondMin = min;
            min = num;
        } else if (num > min && num < secondMin) {
            secondMin = num;
        }
    }

    return (secondMin == Integer.MAX_VALUE) ? Optional.empty() : Optional.of(secondMin);
}
```
In this alternative solution, we iterate through the list only once. We keep track of the smallest and second smallest element while iterating. If we encounter any number that is smaller than the smallest, we update the second smallest and the smallest. If we encounter any number that is between the smallest and the second smallest, we update the second smallest. At the end, if the second smallest is still the maximum value, it means there is no second smallest in the list, so we return an empty Optional. Otherwise, we return the second smallest as the result.

Time complexity: O(n)
Space complexity: O(1)
```

*/

//Test cases

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.nextSmallest(Arrays.asList(1