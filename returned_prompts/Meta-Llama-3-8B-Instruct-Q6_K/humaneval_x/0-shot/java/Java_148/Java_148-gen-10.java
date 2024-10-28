Here is a Java function that meets the requirements:
```java
import java.util.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();
        int index1 = -1, index2 = -1;
        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) {
                index1 = i;
            } else if (planets[i].equals(planet2)) {
                index2 = i;
            }
        }
        if (index1 == -1 || index2 == -1) {
            return new ArrayList<>();
        }
        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets[i]);
        }
        return result;
    }
}
```
Here is an explanation of the code:
1. First, we define an array of planet names.
2. We initialize an empty list to store the result.
3. We iterate through the array of planet names to find the indices of `planet1` and `planet2`. If either of them is not found, we return an empty list.
4. We then iterate from `index1` + 1 to `index2` (exclusive) and add each planet name to the result list.
5. Finally, we return the result list.

Note that this function assumes that the input planet names are correct and that they are in the correct order (i.e., `planet1` is closer to the Sun than `planet2`). If the input planet names are not correct, the function may return incorrect results. Also, this function does not handle the case where `planet1` and `planet2` are the same planet.