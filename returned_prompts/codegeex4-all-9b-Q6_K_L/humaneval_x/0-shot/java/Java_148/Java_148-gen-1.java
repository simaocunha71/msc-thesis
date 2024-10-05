Here is a solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};

        List<String> result = new ArrayList<>();
        int index1 = -1;
        int index2 = -1;

        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) {
                index1 = i;
            }
            if (planets[i].equals(planet2)) {
                index2 = i;
            }
            if (index1 != -1 && index2 != -1) {
                break;
            }
        }

        if (index1 == -1 || index2 == -1) {
            return result;
        }

        if (index1 < index2) {
            for (int i = index1 + 1; i < index2; i++) {
                result.add(planets[i]);
            }
        } else {
            for (int i = index2 + 1; i < index1; i++) {
                result.add(planets[i]);
            }
        }

        return result;
    }
}
```

This solution works by first creating an array of the planets in order of their distance from the Sun. Then, it searches for the indexes of the given planets in the array. If one or both of the planets are not found, it returns an empty list. Otherwise, it adds the planets between the two given planets (in the order of their distance from the Sun) to the result list and returns it.