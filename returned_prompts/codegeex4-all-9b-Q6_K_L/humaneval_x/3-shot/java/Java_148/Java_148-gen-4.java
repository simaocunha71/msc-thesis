        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");

        int planet1_index = planets.indexOf(planet1);
        int planet2_index = planets.indexOf(planet2);

        if (planet1_index == -1 || planet2_index == -1) return new ArrayList<>();

        int start_index = Math.min(planet1_index, planet2_index) + 1;
        int end_index = Math.max(planet1_index, planet2_index);

        return planets.subList(start_index, end_index);
    }
}

