        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();
        int start = planets.indexOf(planet1);
        int end = planets.indexOf(planet2);
        if (start == -1 || end == -1 || start > end) return result;
        for (int i = start; i <= end; i++) {
            result.add(planets.get(i));
        }
        return result;
    }
}

