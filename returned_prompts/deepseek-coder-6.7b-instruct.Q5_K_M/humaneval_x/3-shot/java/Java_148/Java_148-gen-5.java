        List<String> planets_order_from_sun = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int index_planet1 = planets_order_from_sun.indexOf(planet1);
        int index_planet2 = planets_order_from_sun.indexOf(planet2);

        if  (index_planet1  != -1  && index_planet2  != -1 ) {
            return planets_order_from_sun.subList(Math.min(index_planet1, index_planet2) + 1, Math.max(index_planet1, index_planet2));
        } else {
            return new ArrayList<>();
        }
     }
}

