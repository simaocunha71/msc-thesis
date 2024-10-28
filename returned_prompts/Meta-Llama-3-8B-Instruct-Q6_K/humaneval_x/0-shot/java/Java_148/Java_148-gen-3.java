Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();
        for (String planet : planets) {
            if (planet.equals(planet1) || planet.equals(planet2)) {
                continue;
            }
            int index1 = Arrays.asList(planets).indexOf(planet1);
            int index2 = Arrays.asList(planets).indexOf(planet2);
            if (index1 != -1 && index2 != -1) {
                if (index1 < index2) {
                    for (int i = index1 + 1; i < index2; i++) {
                        result.add(planets[i]);
                    }
                } else if (index1 > index2) {
                    for (int i = index2 + 1; i < index1; i++) {
                        result.add(planets[i]);
                    }
                }
            }
        }
        return result;
    }
}
```
This solution first defines an array of planet names and then iterates over the array. For each planet, it checks if the planet is equal to `planet1` or `planet2`. If not, it finds the indices of `planet1` and `planet2` in the array and then iterates over the planets between these two indices, adding them to the result list. Finally, it returns the result list. If `planet1` or `planet2` are not correct planet names, the function returns an empty list. 