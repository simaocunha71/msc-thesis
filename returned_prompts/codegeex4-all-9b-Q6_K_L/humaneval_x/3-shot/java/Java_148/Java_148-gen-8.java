        List<String> result = new ArrayList<>();
        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");

        int start_index = planets.indexOf(planet1);
        int end_index = planets.indexOf(planet2);

        if (start_index == -1 || end_index == -1) return result;

        if (start_index > end_index) {
            int temp = start_index;
            start_index = end_index;
            end_index = temp;
        }

        for (int i = start_index + 1; i < end_index; i++) {
            result.add(planets.get(i));
        }

        return result;
    }
}

