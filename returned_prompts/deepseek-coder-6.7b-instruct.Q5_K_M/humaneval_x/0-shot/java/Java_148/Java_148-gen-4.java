        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();

        // check if both planets are valid
        if (!planets.contains(planet1) || !planets.contains(planet2)) {
            return result;
        }

        // find the index of the planets
        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        // swap the indices if the first index is larger than the second
        if (index1 > index2) {
            int temp = index1;
            index1 = index2;
            index2 = temp;
        }

        // add planets between planet1 and planet2 to the result list
        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets.get(i));
        }

        return result;
    }
}

In the main method, you can test the function:

public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.bf("Jupiter", "Neptune")); // should print [Saturn, Uranus]
        System.out.println(solution.bf("Earth", "Mercury")); // should print [Venus]
        System.out.println(solution.bf("Mercury", "Uranus")); // should print [Venus, Earth, Mars, Jupiter, Saturn]
        System.out.println(solution.bf("Mars", "Pluto")); // should print []
    }

*/

/*
The function works by first creating a list of all the planets. It then checks if both planet1 and planet2 are valid planets. If not, it returns an empty list.

If the planets are valid, it finds the index of planet1 and planet2 in the list of planets. If the index of planet1 is greater than the index of planet2, it swaps the indices.

Finally, it iter