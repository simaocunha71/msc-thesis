import java.util.*;
import java.lang.*;

class Solution {
    /**
    There are eight planets in our solar system: the closerst to the Sun
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn,
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2.
    The function should return a tuple containing all planets whose orbits are
    located between the orbit of planet1 and the orbit of planet2, sorted by
    the proximity to the sun.
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names.
    Examples
    bf("Jupiter", "Neptune") ==> ["Saturn", "Uranus"]
    bf("Earth", "Mercury") ==> ["Venus"]
    bf("Mercury", "Uranus") ==> ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
     */
    public List<String> bf(String planet1, String planet2) {
        List<String> list = new ArrayList();
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        int i = Arrays.asList(planets).indexOf(planet1);
        int j = Arrays.asList(planets).indexOf(planet2);
        if (i == -1 || j == -1) {
            return list;
        }
        for (int k = i; k <= j; k++) {
            list.add(planets[k]);
        }
        return list;
    }
}
