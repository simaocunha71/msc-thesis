```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();
        int p1 = -1, p2 = -1;
        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) {
                p1 = i;
            }
            if (planets[i].equals(planet2)) {
                p2 = i;
            }
        }
        if (p1 == -1 || p2 == -1) {
            return result;
        }
        if (p1 > p2) {
            int temp = p1;
            p1 = p2;
            p2 = temp;
        }
        for (int i = p1 + 1; i < p2; i++) {
            result.add(planets[i]);
        }
        return result;
    }
}
```