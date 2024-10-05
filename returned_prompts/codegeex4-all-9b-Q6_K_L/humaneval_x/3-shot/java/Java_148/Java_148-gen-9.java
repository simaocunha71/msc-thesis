        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        return planets.subList(planets.indexOf(planet1) + 1, planets.indexOf(planet2));
    }
}

