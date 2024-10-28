        List<String> planets = Arrays.asList(
            "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
        );
        int i1 = planets.indexOf(planet1);
        int i2 = planets.indexOf(planet2);
        if (i1 < 0 || i2 < 0) return Collections.emptyList();
        List<String> result = new ArrayList<>();
        for (int i = i1 + 1; i < i2; i++) {
            result.add(planets.get(i));
        }
        return result;
    }
}

