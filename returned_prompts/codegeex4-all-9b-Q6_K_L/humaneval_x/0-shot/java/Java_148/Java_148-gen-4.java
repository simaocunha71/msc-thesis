```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);
        if (index1 == -1 || index2 == -1) {
            return Collections.emptyList();
        }
        List<String> result = new ArrayList<>();
        for (int i = Math.min(index1, index2) + 1; i < Math.max(index1, index2); i++) {
            result.add(planets.get(i));
        }
        return result;
    }
}
```