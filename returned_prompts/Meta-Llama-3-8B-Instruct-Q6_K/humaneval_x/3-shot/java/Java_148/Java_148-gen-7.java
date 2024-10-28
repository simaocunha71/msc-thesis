        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();
        int index1 = -1, index2 = -1;
        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) index1 = i;
            if (planets[i].equals(planet2)) index2 = i;
        }
        if (index1 == -1 || index2 == -1) return new ArrayList<>();
        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets[i]);
        }
        Collections.sort(result);
        return result;
    }
}

