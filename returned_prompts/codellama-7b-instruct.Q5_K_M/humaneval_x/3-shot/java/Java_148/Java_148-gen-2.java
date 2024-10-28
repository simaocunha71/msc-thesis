        List<String> result = new ArrayList<>();
        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int idx1 = planets.indexOf(planet1);
        int idx2 = planets.indexOf(planet2);

        if (idx1 == -1 || idx2 == -1) return result;

        for (int i = idx1 + 1; i <= idx2; i++) {
            result.add(planets.get(i));
        }
        for (int i = idx2 - 1; i > idx1; i--) {
            result.add(planets.get(i));
        }

        return result;
    }
}

