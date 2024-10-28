        List<String> result = new ArrayList<>();
        if (planet1.equals("Sun") || planet2.equals("Sun")) {
            return result;
        }

        int index1 = getPlanetIndex(planet1);
        int index2 = getPlanetIndex(planet2);

        for (int i = index1 + 1; i < index2; i++) {
            result.add(planet_order[i]);
        }

        result.add(planet_order[index1]);

        return result;
    }

    private int getPlanetIndex(String planet) {
        int result = -1;
        for (int i = 0; i < planet_order.length; i++) {
            if (planet_order[i].equals(planet)) {
                result = i;
                break;
            }
        }
        return result;
    }

    private final String[] planet_order = {
            "Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune"
    };
}

