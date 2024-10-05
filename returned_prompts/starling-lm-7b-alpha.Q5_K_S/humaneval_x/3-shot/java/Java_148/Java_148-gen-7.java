        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int planet1_index = planets.indexOf(planet1);
        int planet2_index = planets.indexOf(planet2);

        if (planet1_index < 0 || planet2_index < 0) return Collections.emptyList();

        List<String> result = new ArrayList<>();
        for (int i = planet1_index; i <= planet2_index; i++) {
            result.add(planets.get(i));
        }
        return result;
    }
}

