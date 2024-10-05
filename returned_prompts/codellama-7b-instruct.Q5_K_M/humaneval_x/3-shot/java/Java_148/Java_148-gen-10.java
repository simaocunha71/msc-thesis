        List<String> result = new ArrayList<>();
        boolean planet1_found = false;
        boolean planet2_found = false;

        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};

        for (String planet : planets) {
            if (planet.equals(planet1)) planet1_found = true;
            if (planet.equals(planet2)) planet2_found = true;

            if (planet1_found && planet2_found) break;
        }

        if (!planet1_found || !planet2_found) return result;

        for (String planet : planets) {
            if (!planet1_found && !planet2_found) {
                result.add(planet);
            } else if (!planet1_found && planet2_found) {
                if (planet.compareTo(planet2) > 0) break;
                else result.add(planet);
            } else if (planet1_found && !planet2_found) {
                if (planet.compareTo(planet1) < 0) break;
                else result.add(planet);
            } else {
                if (planet.compareTo(planet1) > 0 && planet.compareTo(planet2) < 0) {
                    result.add(planet);
                }
            }
        }
        return result;
    }
}

