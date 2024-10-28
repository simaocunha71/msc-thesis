        List<String> result = new ArrayList<>();

        int index_of_planet1 = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune").indexOf(planet1);
        int index_of_planet2 = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune").indexOf(planet2);

        if (index_of_planet1 == -1 || index_of_planet2 == -1) return result;

        for (String planet : Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")) {
            if (Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune").indexOf(planet) >= index_of_planet1 &&
                Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune").indexOf(planet) <= index_of_planet2) {
                result.add(planet);
            }
        }
        Collections.sort(result, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune").indexOf(o1) -
                    Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune").indexOf(o2);
            }
        });
        return result;
    }
}

