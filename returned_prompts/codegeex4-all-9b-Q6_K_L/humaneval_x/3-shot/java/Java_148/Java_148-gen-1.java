        List<String> planets = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int index1 = planets.indexOf(planet1);
        int index2 = planets.indexOf(planet2);

        if (index1 == -1 || index2 == -1) {
            return Collections.emptyList();
        } else {
            if (index1 > index2) {
                int temp = index1;
                index1 = index2;
                index2 = temp;
            }
            return planets.subList(index1 + 1, index2);
        }
    }
}

