        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();

        if (!planets.contains(planet1) || !planets.contains(planet2))
            return result;

        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        if (index1 > index2) {
            int temp = index1;
            index1 = index2;
            index2 = temp;
        }

        for (int i = index1 + 1; i < index2; i++)
            result.add(planets.get(i));

        return result;
    }
}

This solution works by first checking if the input strings are valid planet names. If they are, it finds the index of the first and second planet in the list of planets, and then adds all the planets between them (exclusive) to the result list. If the first planet is further away from the Sun than the second, the function swaps the two indices to ensure the loop works correctly. Finally, it returns the result list.

In the case where the input strings are not valid planet names, the function returns an empty list.

It's worth noting that this solution assumes that the order of the planets in the list is the same as their proximity to the Sun. If that's not the case, the function would have to be adjusted accordingly.
*/

// Test Cases
// bf("Jupiter", "Neptune")  -> ["Saturn", "Uranus"]
// bf("Earth", "Mercury")  -> ["Venus"]
// bf("Mercury", "Uranus")  -> ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
// bf("Mars", "Pluto")  -> []
// bf("Jupiter", "Pluto")  -> []

// Complexity: O(n) as we traverse the planets list once.
// Space complexity: O(n) as