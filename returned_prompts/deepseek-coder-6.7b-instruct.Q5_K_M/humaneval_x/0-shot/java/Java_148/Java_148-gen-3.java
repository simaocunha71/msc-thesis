        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();

        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        if(index1 == -1 || index2 == -1)
            return result;

        if(index1 > index2) {
            int temp = index1;
            index1 = index2;
            index2 = temp;
        }

        for(int i = index1 + 1; i < index2; i++) {
            result.add(planets.get(i));
        }

        return result;
    }
}

In this code, we first create a list of the planets in order of proximity to the sun. Then we find the index of the two given planets in this list. If either of the given planets is not found in the list, we return an empty list.

If the index of planet1 is larger than the index of planet2, we swap their indices to ensure that we are iterating from the smaller index to the larger one.

Finally, we iterate from the next planet of planet1 to the planet before planet2, adding each planet we encounter to the result list. We then return this result list.
*/

//Solution 2:

import java.util.*;
import java.lang.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {

        Map<String, Integer> planets = new HashMap<>();
        planets.put("Mercury", 1);
        planets.put("Venus", 2);
        planets.put("Earth", 3);
        planets.put("Mars", 4);
        planets.put("Jupiter", 5);
        planets.put("Saturn", 6);
        planets.put("Uranus", 7);
        planets.put("Neptune", 8);

        List<String> result = new ArrayList<>();

        if(!planets.contains