import java.util.*;

class Solution {
    /**
    There are eight planets in our solar system: the closests to the Sun
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
        List<String> result = new ArrayList<>();
        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int i1 = planets.indexOf(planet1);
        int i2 = planets.indexOf(planet2);
        if (i1 == -1 || i2 == -1)
            return result;
        int start = i1 < i2 ? i1 + 1 : i1;
        int end = i1 < i2 ? i2 : i2 + 1;
        for (int i = start; i < end; i++) {
            result.add(planets.get(i));
        }
        Collections.sort(result, (a, b) -> planets.indexOf(a) - planets.indexOf(b));
        return result;
    }
}