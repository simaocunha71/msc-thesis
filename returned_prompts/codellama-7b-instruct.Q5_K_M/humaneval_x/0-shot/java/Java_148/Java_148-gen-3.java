import java.util.*;
import java.lang.*;

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
        List<String> planets = new ArrayList<String>();
        planets.add("Mercury");
        planets.add("Venus");
        planets.add("Earth");
        planets.add("Mars");
        planets.add("Jupiter");
        planets.add("Saturn");
        planets.add("Uranus");
        planets.add("Neptune");
        int pos1 = planets.indexOf(planet1);
        int pos2 = planets.indexOf(planet2);
        if(pos1 == -1 || pos2 == -1) {
            return new ArrayList<>();
        }
        if(pos1 > pos2) {
            return planets.subList(pos2, pos1+1);
        }
        return planets.subList(pos1+1, pos2);
    }
}
