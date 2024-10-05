        List<String> result = new ArrayList<>();
        switch (planet1) {
            case "Mercury":
                switch (planet2) {
                    case "Venus":
                        result.add("Earth");
                        result.add("Mars");
                        result.add("Jupiter");
                        result.add("Saturn");
                        result.add("Uranus");
                        result.add("Neptune");
                        break;
                    case "Uranus":
                        result.add("Earth");
                        result.add("Mars");
                        result.add("Jupiter");
                        result.add("Saturn");
                        break;
                    default:
                        break;
                }
                break;
            case "Venus":
                switch (planet2) {
                    case "Earth":
                        result.add("Mars");
                        result.add("Jupiter");
                        result.add("Saturn");
                        result.add("Uranus");
                        result.add("Neptune");
                        break;
                    case "Mars":
                        result.add("Jupiter");
                        result.add("Saturn");
                        result.add("Uranus");
                        result.add("Neptune");
                        break;
                    case "Jupiter":
                        result.add("Saturn");
                        result.add("Uranus");
                        result.add("Neptune");
                        break;
                    case "Saturn":
                        result.add("Uranus");
                        result.add("Neptune");
                        break;
                    default:
                        break;
                }
                break;
            case "Earth":
                switch (planet2) {
                    case "Mars":
                        result.add("Jupiter");
                        result.add("Saturn");
                        result.add("Uranus");
                        result.add("Neptune");
                        break;
                    case "Jupiter":
                