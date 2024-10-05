Here is a possible solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        // Check if the list is empty
        if (lst.isEmpty()) {
            return lst;
        }

        // Create a new list to store the result
        List<Integer> result = new ArrayList<>();

        // Create a new list to store the remaining integers
        List<Integer> remaining = new ArrayList<>(lst);

        // Initialize a boolean to keep track of the current direction
        boolean minDirection = true;

        // Loop until the remaining list is empty
        while (!remaining.isEmpty()) {
            // Get the minimum or maximum value depending on the direction
            int value = minDirection ? Collections.min(remaining) : Collections.max(remaining);

            // Add the value to the result list
            result.add(value);

            // Remove the value from the remaining list
            remaining.remove(Integer.valueOf(value));

            // Toggle the direction
            minDirection = !minDirection;
        }

        // Return the result list
        return result;
    }
}
```

This solution works by creating a new list to store the remaining integers and a boolean to keep track of the current direction. It then loops until the remaining list is empty, getting the minimum or maximum value depending on the direction, adding it to the result list, removing it from the remaining list, and toggling the direction. Finally, it returns the result list.