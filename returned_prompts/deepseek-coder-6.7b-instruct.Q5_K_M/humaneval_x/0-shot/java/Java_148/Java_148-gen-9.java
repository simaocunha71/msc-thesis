        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();

        int idx1 = planets.indexOf(planet1);
        int idx2 = planets.indexOf(planet2);

        if (idx1 == -1 || idx2 == -1) {
            return result;
        }

        if (idx1 > idx2) {
            int temp = idx1;
            idx1 = idx2;
            idx2 = temp;
        }

        for (int i = idx1 + 1; i < idx2; i++) {
            result.add(planets.get(i));
        }

        return result;
    }
}


