        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();
        int idx1, idx2;

        idx1 = planets.indexOf(planet1);
        idx2 = planets.indexOf(planet2);

        if (idx1 < 0 || idx2 < 0) return result;

        result.addAll(planets.subList(Math.min(idx1, idx2) + 1, Math.max(idx1, idx2)));
        return result;
    }
}

