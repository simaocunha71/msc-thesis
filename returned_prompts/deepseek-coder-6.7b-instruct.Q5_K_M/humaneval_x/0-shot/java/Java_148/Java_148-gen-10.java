        List<String> result = new ArrayList<>();
        List<String> solarSystem = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int index1 = solarSystem.indexOf(planet1);
        int index2 = solarSystem.indexOf(planet2);

        if (index1 == -1 || index2 == -1) {
            return result;
        }

        if (index1 > index2) {
            int temp = index1;
            index1 = index2;
            index2 = temp;
        }

        for (int i = index1 + 1; i < index2; i++) {
            result.add(solarSystem.get(i));
        }

        return result;
    }
}

This solution creates a list of the planets in the solar system and then finds the indexes of the given planet names in that list. If either of the planet names is not found in the list, it returns an empty list. If the indexes are out of order, it swaps them. It then adds all the planets between the two indexes to the result list and returns that list.

This solution assumes that the input strings are valid planet names and that the planets are listed in the order they are closer to the sun. It also assumes that the input strings are case sensitive.

This solution has a time complexity of O(n) as it iterates through the list of planets once. The space complexity is also O(n) as it creates a new list to store the result.

This solution does not handle the case where planet1 and planet2 are the same planet. It would add the planet once if they are the same. If you want to handle this case differently, you can add a special case to handle it.
