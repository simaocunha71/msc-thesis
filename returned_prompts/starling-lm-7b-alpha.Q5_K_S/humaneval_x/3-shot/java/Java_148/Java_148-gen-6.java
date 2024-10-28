        if (planet1.equals("Mercury")) {
            if (planet2.equals("Venus")) {
                return Arrays.asList("Venus");
            } else if (planet2.equals("Earth")) {
                return Arrays.asList("Earth");
            } else if (planet2.equals("Mars")) {
                return Arrays.asList("Mars");
            } else if (planet2.equals("Jupiter")) {
                return Arrays.asList("Jupiter");
            } else if (planet2.equals("Saturn")) {
                return Arrays.asList("Saturn");
            } else if (planet2.equals("Uranus")) {
                return Arrays.asList("Uranus");
            } else if (planet2.equals("Neptune")) {
                return Arrays.asList("Neptune");
            }
        } else if (planet1.equals("Venus")) {
            if (planet2.equals("Earth")) {
                return Arrays.asList("Earth", "Mars");
            } else if (planet2.equals("Mars")) {
                return Arrays.asList("Mars", "Jupiter");
            } else if (planet2.equals("Jupiter")) {
                return Arrays.asList("Jupiter", "Saturn");
            } else if (planet2.equals("Saturn")) {
                return Arrays.asList("Saturn", "Uranus");
            } else if (planet2.equals("Uranus")) {
                return Arrays.asList("Uranus", "Neptune");
            } else if (planet2.equals("Neptune")) {
                return Collections.emptyList();
            }
        } else if (planet1.equals("Earth")) {
            if (planet2.equals("Mars")) {
                return Arrays.asList("Mars");
            } else if (planet2.equals("Jupiter")) {
                return Arrays.asList("Jupiter