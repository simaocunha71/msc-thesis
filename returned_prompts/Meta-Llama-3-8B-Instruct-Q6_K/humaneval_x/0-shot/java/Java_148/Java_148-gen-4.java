Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();

        if (!isValidPlanet(planet1) || !isValidPlanet(planet2)) {
            return new ArrayList<>();
        }

        int index1 = Arrays.asList(planets).indexOf(planet1);
        int index2 = Arrays.asList(planets).indexOf(planet2);

        if (index1 == -1 || index2 == -1) {
            return new ArrayList<>();
        }

        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets[i]);
        }

        return result;
    }

    private boolean isValidPlanet(String planet) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        return Arrays.asList(planets).contains(planet);
    }
}
```

This solution first checks if both planet1 and planet2 are valid planets. If not, it returns an empty list. Then it finds the indices of planet1 and planet2 in the array of planets. It then iterates through the array from the index of planet1 + 1 to the index of planet2, adding each planet to the result list. Finally, it returns the result list. The isValidPlanet method checks if a given planet is in the array of planets. If not, it returns false. If so, it returns true.