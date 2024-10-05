        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        int p1 = -1, p2 = -1;
        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) p1 = i;
            if (planets[i].equals(planet2)) p2 = i;
        }
        if (p1 == -1 || p2 == -1) return new ArrayList<>();
        List<String> result = new ArrayList<>();
        for (int i = p1 + 1; i < p2; i++) {
            result.add(planets[i]);
        }
        return result;
    }
}

