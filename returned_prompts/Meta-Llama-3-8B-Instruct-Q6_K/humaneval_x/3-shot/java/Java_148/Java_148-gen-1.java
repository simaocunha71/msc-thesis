        List<String> result = new ArrayList<>();
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        int index1 = -1, index2 = -1;
        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) index1 = i;
            if (planets[i].equals(planet2)) index2 = i;
        }
        if (index1 == -1 || index2 == -1) return result;
        int start = Math.min(index1, index2);
        int end = Math.max(index1, index2);
        for (int i = start + 1; i < end; i++) {
            result.add(planets[i]);
        }
        return result;
    }
}