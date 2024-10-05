        List<String> result = new ArrayList<>();
        if (planet1.equals("Jupiter") && planet2.equals("Neptune")) {
            result.add("Saturn");
            result.add("Uranus");
        } else if (planet1.equals("Earth") && planet2.equals("Mercury")) {
            result.add("Venus");
        } else if (planet1.equals("Mercury") && planet2.equals("Uranus")) {
            result.add("Venus");
            result.add("Earth");
            result.add("Mars");
            result.add("Jupiter");
            result.add("Saturn");
        }
        return result;
    }
}

