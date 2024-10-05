    List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");

    int index1 = planets.indexOf(planet1);
    int index2 = planets.indexOf(planet2);

    if (index1 == -1 || index2 == -1) {
        return new ArrayList<>();
    }

    if (index1 > index2) {
        int temp = index1;
        index1 = index2;
        index2 = temp;
    }

    return planets.subList(index1 + 1, index2);
    }
}

Here, we are using the `indexOf()` method to get the index of the two planets given as input. If any of the planets is not found in the list of planets, then -1 is returned and the function returns an empty list. If the indices of planet1 and planet2 are in the wrong order (i.e., planet1 is found after planet2), then the function swaps the indices. Finally, it returns a sublist of the planets whose indices are between the indices of planet1 and planet2, inclusive.
*/

