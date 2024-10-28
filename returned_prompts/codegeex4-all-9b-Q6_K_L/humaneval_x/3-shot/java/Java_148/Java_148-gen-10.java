        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");

        int i1 = planets.indexOf(planet1);
        int i2 = planets.indexOf(planet2);

        if (i1 == -1 || i2 == -1) return new ArrayList<>();

        List<String> result = new ArrayList<>();

        for (int i = Math.min(i1, i2) + 1; i < Math.max(i1, i2); i++) {
            result.add(planets.get(i));
        }

        return result;
    }
}

