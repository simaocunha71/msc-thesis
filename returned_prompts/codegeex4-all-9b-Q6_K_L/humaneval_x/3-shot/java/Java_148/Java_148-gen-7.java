        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");

        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        if (index1 == -1 || index2 == -1) {
            return Collections.emptyList();
        }

        List<String> result = new ArrayList<>();
        if (index1 < index2) {
            for (int i = index1 + 1; i < index2; i++) {
                result.add(planets.get(i));
            }
        } else {
            for (int i = index2 + 1; i < index1; i++) {
                result.add(planets.get(i));
            }
        }
        return result;
    }
}

