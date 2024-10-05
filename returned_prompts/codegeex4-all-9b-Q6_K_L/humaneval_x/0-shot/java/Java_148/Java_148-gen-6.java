Here's a solution to your problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();
        
        int planet1Index = planets.indexOf(planet1);
        int planet2Index = planets.indexOf(planet2);
        
        if (planet1Index == -1 || planet2Index == -1) {
            return result;
        }
        
        if (planet1Index < planet2Index) {
            for (int i = planet1Index + 1; i < planet2Index; i++) {
                result.add(planets.get(i));
            }
        } else {
            for (int i = planet2Index + 1; i < planet1Index; i++) {
                result.add(planets.get(i));
            }
        }
        
        return result;
    }
}
```

This solution works by first defining a list of the planets in order of their distance from the sun. It then finds the indices of the given planet names in this list, and if either of them is not found, it returns an empty list.

If both planet names are found, it checks which one is closer to the sun and then adds all the planets between the two indices to the result list.

Finally, it returns the result list.