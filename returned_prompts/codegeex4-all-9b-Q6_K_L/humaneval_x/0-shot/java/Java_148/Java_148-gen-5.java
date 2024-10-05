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
        }
        if (index1 == -1 || index2 == -1) {
            return result;
        }
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