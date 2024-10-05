```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        List<String> planetOrder = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int index1 = planetOrder.indexOf(planet1);
        int index2 = planetOrder.indexOf(planet2);
        
        if (index1 == -1 || index2 == -1) {
            return new ArrayList<>();
        }
        
        if (index1 > index2) {
            int temp = index1;
            index1 = index2;
            index2 = temp;
        }
        
        List<String> result = new ArrayList<>();
        for (int i = index1 + 1; i < index2; i++) {
            result.add(planetOrder.get(i));
        }
        
        return result;
    }
}
```