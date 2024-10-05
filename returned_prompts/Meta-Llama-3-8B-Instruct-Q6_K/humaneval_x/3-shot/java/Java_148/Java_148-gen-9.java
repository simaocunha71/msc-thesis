        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();
        int idx1 = -1, idx2 = -1;
        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) idx1 = i;
            if (planets[i].equals(planet2)) idx2 = i;
        }
        if (idx1 == -1 || idx2 == -1) return new ArrayList<>();
        for (int i = idx1 + 1; i < idx2; i++) {
            result.add(planets[i]);
        }
        return result;
    }
}

