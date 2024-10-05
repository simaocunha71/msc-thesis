```java
import java.util.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        List<String> result = new ArrayList<>();
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        int index1 = -1, index2 = -1;
        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) {
                index1 = i;
            }
            if (planets[i].equals(planet2)) {
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
The solution uses an array of planet names to store the order of the planets in the solar system. It then iterates over the array to find the indices of the two input planets. If either of the input planets is not found in the array, it returns an empty list. If both planets are found, it iterates over the array between their indices and adds the planet names to the result list. Finally, it returns the result list. The list is sorted in the order of proximity to the sun, which is the order of the planets in the array. The function returns an empty list if planet1 or planet2 are not correct planet names. The function is case-sensitive.