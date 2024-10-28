Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();

        if (!Arrays.asList(planets).contains(planet1) || !Arrays.asList(planets).contains(planet2)) {
            return new ArrayList<>();
        }

        int index1 = Arrays.asList(planets).indexOf(planet1);
        int index2 = Arrays.asList(planets).indexOf(planet2);

        if (index1 > index2) {
            int temp = index1;
            index1 = index2;
            index2 = temp;
        }

        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets[i]);
        }

        return result;
    }
}
```

This solution defines an array of planet names and uses the `Arrays.asList()` method to convert the array to a list. The function then checks if both input planet names are in the list. If not, it returns an empty list.

Next, it finds the indices of the input planet names in the list. If the index of the first planet is greater than the index of the second planet, it swaps them.

Finally, it iterates over the indices between the indices of the input planet names, adds the corresponding planet names to the result list, and returns the list. The result list contains the planet names whose orbits are located between the orbits of the input planet names, sorted by proximity to the Sun. If the input planet names are not correct, the function returns an empty list.