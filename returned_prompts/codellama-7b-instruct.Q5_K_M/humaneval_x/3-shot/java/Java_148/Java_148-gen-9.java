        List<String> result = new ArrayList<>();
        if (!(planet1.equals("Mercury") || planet2.equals("Mercury"))) {
            return result;
        }
        if (planet1.equals("Mercury")) {
            result.add("Venus");
            if (planet2.equals("Neptune")) {
                result.add("Earth");
                result.add("Mars");
                result.add("Jupiter");
                result.add("Saturn");
            }
        }
        if (planet1.equals("Earth") || planet1.equals("Mars")) {
            result.add("Venus");
            if (planet2.equals("Neptune")) {
                result.add("Jupiter");
                result.add("Saturn");
            }
        }
        if (planet1.equals("Jupiter")) {
            if (planet2.equals("Neptune")) {
                result.add("Saturn");
            }
        }
        if (planet1.equals("Saturn")) {
            result.add("Uranus");
            result.add("Neptune");
        }
        return result;
    }
}

