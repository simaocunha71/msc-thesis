        List<String> planets = Arrays.asList(
                "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        if (index1 == -1 || index2 == -1) {
            return new ArrayList<>();
        }

        return planets.subList(Math.min(index1, index2), Math.max(index1, index2) + 1);
    }
}

