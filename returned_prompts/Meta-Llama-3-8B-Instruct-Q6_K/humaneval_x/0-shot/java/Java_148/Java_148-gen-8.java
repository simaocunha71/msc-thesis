Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();

        if (!Arrays.asList(planets).contains(planet1) || !Arrays.asList(planets).contains(planet2)) {
            return result;
        }

        int index1 = Arrays.asList(planets).indexOf(planet1);
        int index2 = Arrays.asList(planets).indexOf(planet2);

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

This solution defines an array of planet names and uses the `Arrays.asList` method to convert it into a list. It then checks if the input planet names are in the list. If not, it returns an empty list.

Next, it finds the indices of the input planet names in the list. If the index of the first planet is greater than the index of the second planet, it swaps them.

Finally, it loops through the list from the index of the first planet to the index of the second planet, adding each planet name to the result list. The result list is then returned.

The function is case-sensitive and assumes that the input planet names are correct (i.e., they are in the list of planets). If the input planet names are not correct, the function returns an empty list. If the input planet names are correct but not in the correct order, the function still returns the correct result. For example, `bf("Jupiter", "Neptune")` returns `["Saturn", "Uranus"]`, even though "Jupiter" comes before "Neptune" in the list of planets. This is because the function checks the indices of the input planet names, not their positions in the list. If you want to check the positions in the list, you would need to modify the function accordingly.