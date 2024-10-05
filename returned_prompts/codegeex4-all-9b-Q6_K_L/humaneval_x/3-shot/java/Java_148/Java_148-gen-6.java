        String[] planets = new String[] {
                "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
        };

        int index1 = -1;
        int index2 = -1;

        for (int i = 0; i < planets.length; i++) {
            if (planets[i].equals(planet1)) index1 = i;
            if (planets[i].equals(planet2)) index2 = i;
        }

        if (index1 == -1 || index2 == -1) return new ArrayList<>();

        int start = Math.min(index1, index2) + 1;
        int end = Math.max(index1, index2);

        List<String> result = new ArrayList<>();

        for (int i = start; i < end; i++) {
            result.add(planets[i]);
        }

        return result;

    }
}

