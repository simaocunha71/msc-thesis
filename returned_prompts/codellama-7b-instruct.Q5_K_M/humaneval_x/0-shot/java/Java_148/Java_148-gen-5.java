import java.util.*;

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
        List<String> list = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        map.put("Mercury", 1);
        map.put("Venus", 2);
        map.put("Earth", 3);
        map.put("Mars", 4);
        map.put("Jupiter", 5);
        map.put("Saturn", 6);
        map.put("Uranus", 7);
        map.put("Neptune", 8);

        if (planet1.equals("Mercury") || planet2.equals("Mercury")) {
            list.add("Venus");
            list.add("Earth");
            list.add("Mars");
            list.add("Jupiter");
            list.add("Saturn");
        }
        if (planet1.equals("Venus") || planet2.equals("Venus")) {
            list.add("Earth");
            list.add("Mars");
            list.add("Jupiter