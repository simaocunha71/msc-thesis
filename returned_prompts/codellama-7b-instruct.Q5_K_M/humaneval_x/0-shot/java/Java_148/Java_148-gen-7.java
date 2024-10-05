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
        // Your code here
        // list of all planets
        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        // list of planets between orbit of planet1 and planet2
        List<String> orbitingPlanets = new ArrayList<>();

        // check if planet1 and planet2 are in list of planets
        if (!planets.contains(planet1) || !planets.contains(planet2)) {
            return orbitingPlanets;
        }

        // get index of planet1 and planet2
        int indexOfPlanet1 = planets.indexOf(planet1);
        int indexOfPlanet2 = planets.indexOf(planet2);

        // if planet1 is before planet2 in list of planets
        if (indexOfPlanet1 < indexOfPlanet2) {
            // add planets between orbit of planet1 and planet2
            for (int i =