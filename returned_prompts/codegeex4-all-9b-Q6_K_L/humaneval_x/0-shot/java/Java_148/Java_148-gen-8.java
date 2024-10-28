```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();

        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        if (index1 == -1 || index2 == -1) {
            return result;
        }

        if (index1 > index2) {
            int temp = index1;
            index1 = index2;
            index2 = temp;
        }

        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets.get(i));
        }

        return result;
    }
}
```