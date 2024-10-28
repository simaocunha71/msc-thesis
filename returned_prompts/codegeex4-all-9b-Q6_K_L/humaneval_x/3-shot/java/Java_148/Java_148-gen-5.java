        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");

        if (!planets.contains(planet1) || !planets.contains(planet2)) return new ArrayList<>();

        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        return index1 < index2 ? planets.subList(index1 + 1, index2) : planets.subList(index2 + 1, index1);
    }
}

