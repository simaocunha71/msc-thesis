        List<String> planets = new ArrayList<>(Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"));
        String[] validPlanets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};

        if (!Arrays.asList(validPlanets).contains(planet1) || !Arrays.asList(validPlanets).contains(planet2)) {
            return new ArrayList<>();
        }

        int index1 = Arrays.asList(validPlanets).indexOf(planet1);
        int index2 = Arrays.asList(validPlanets).indexOf(planet2);

        List<String> result = new ArrayList<>();
        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets.get(i));
        }

        return result;
    }
}

