        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");

        int i = planets.indexOf(planet1);
        int j = planets.indexOf(planet2);

        if (i < 0 || j < 0 || i > j) return new ArrayList<>();

        return planets.subList(i, j + 1);
    }
}


