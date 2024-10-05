        List<String> result = new ArrayList<>();
        Set<String> planets = new HashSet<>(Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"));

        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        if (index1 == -1 || index2 == -1) {
            return result;
        }

        for (int i = index1; i <= index2; i++) {
            result.add(planets.toArray(new String[0])[i]);
        }
        return result;
    }
}

