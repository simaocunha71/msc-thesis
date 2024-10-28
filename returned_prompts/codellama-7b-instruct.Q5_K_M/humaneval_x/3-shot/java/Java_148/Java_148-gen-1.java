        List<String> result = new ArrayList<>();
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};

        int index_of_first_planet = -1;
        int index_of_second_planet = -1;

        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) {
                index_of_first_planet = i;
            }
            if (planets[i].equals(planet2)) {
                index_of_second_planet = i;
            }
        }
        if (index_of_first_planet == -1 || index_of_second_planet == -1) {
            return result;
        }
        for (int i = index_of_first_planet; i <= index_of_second_planet; i++) {
            result.add(planets[i]);
        }
        return result;
    }
}

