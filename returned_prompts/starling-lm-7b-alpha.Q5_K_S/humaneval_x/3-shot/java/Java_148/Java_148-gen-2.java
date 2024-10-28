        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        List<String> result = new ArrayList<>();
        int i1 = planets.indexOf(planet1);
        int i2 = planets.indexOf(planet2);
        if (i1 == -1 || i2 == -1) return result;
        if (i1 > i2) {
            int tmp = i1;
            i1 = i2;
            i2 = tmp;
        }
        for (int i = i1; i <= i2; i++) {
            result.add(planets.get(i));
        }
        return result;
    }
}

