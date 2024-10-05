        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();

        for (String p : planets) {
            if (p.equals(planet1) || p.equals(planet2)) {
                continue;
            }

            if (Arrays.asList(planets).indexOf(planet1) < Arrays.asList(planets).indexOf(p) && 
                Arrays.asList(planets).indexOf(p) < Arrays.asList(planets).indexOf(planet2)) {
                result.add(p);
            }
        }

        if (Arrays.asList(planets).indexOf(planet1) >= 0 && 
            Arrays.asList(planets).indexOf(planet2) >= 0) {
            Collections.sort(result);
            return result;
        } else {
            return new ArrayList<>();
        }
    }
}